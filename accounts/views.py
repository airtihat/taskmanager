from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.models import Group
from .models import GroupInvite

# ✅ تسجيل الدخول مع توجيه حسب الصلاحية
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)

            # ✅ التوجيه حسب المجموعة أو نوع الحساب
            if user.groups.filter(name='محاسبة').exists():
                return redirect('accounts:dashboard')
            elif user.groups.filter(name='تبرعات').exists():
                return redirect('sadaqa:dashboard')
            elif user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('home')  # أو أي صفحة افتراضية

        else:
            messages.error(request, '❌ اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'accounts/login.html')


# ✅ تسجيل مستخدم جديد مع إرسال بريد
def register_view(request):
    group_name = request.GET.get('group')  # أخذ اسم المجموعة من الرابط

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # ✅ إضافة المستخدم للمجموعة إذا تم تحديدها
            if group_name:
                group, created = Group.objects.get_or_create(name=group_name)
                user.groups.add(group)

            messages.success(request, '✅ تم إنشاء الحساب بنجاح!')

            # إرسال بريد ترحيبي
            send_mail(
                subject='🎉 مرحبًا بك في نظام إدارة المهام',
                message=f'شكرًا لانضمامك لمجموعة {group_name}. يمكنك الآن البدء.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )

            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'group_name': group_name,  # نمرر الاسم للقالب
    })


# ✅ لوحة المستخدم
@login_required
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html', {
        'tasks_count': request.user.tasks.count() if hasattr(request.user, 'tasks') else 0,
    })


# ✅ إرسال تذكير بالبريد
@login_required
def send_email_reminder(request):
    if request.method == 'POST':
        subject = '🔔 تذكير بالمهمة'
        message = 'مرحبًا، هذه رسالة تذكير لك بتنفيذ المهمة المحددة اليوم.'
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, '✅ تم إرسال التذكير إلى بريدك الإلكتروني.')
        except Exception as e:
            messages.error(request, f'❌ حدث خطأ أثناء الإرسال: {e}')
        return redirect('accounts:user_dashboard')

    return render(request, 'accounts/send_reminder.html')


# ✅ عرض الملف الشخصي
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })


# ✅ عرض قائمة المستخدمين (للمشرف فقط)
@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})


@staff_member_required
def pending_approvals(request):
    invites = GroupInvite.objects.filter(approved=False, user__isnull=False)
    return render(request, 'accounts/pending_approvals.html', {'invites': invites})


@staff_member_required
def approve_invite(request, invite_id):
    invite = GroupInvite.objects.get(id=invite_id)
    if invite.user:
        group, created = Group.objects.get_or_create(name=invite.group_name)
        invite.user.groups.add(group)
        invite.approved = True
        invite.save()
        messages.success(request, '✅ تمت الموافقة وتمت إضافة المستخدم للمجموعة.')
    return redirect('accounts:pending_approvals')


# ✅ إرسال الدعوة للمجموعة
@login_required
def send_invite(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        group_name = request.POST.get('group_name')

        invite = GroupInvite.objects.create(
            email=email,
            group_name=group_name,
            invited_by=request.user
        )

        # إرسال البريد الإلكتروني
        invite_link = invite.get_invite_link()
        subject = f"دعوة للانضمام إلى مجموعة {group_name}"
        message = f"مرحبًا،\n\nلقد تمت دعوتك للانضمام إلى مجموعة {group_name}.\nرابط التسجيل:\n{invite_link}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

        messages.success(request, f"✅ تم إرسال الدعوة إلى {email}.")
        return redirect('accounts:send_invite')

    return render(request, 'accounts/send_invite.html')


# ✅ إعدادات النظام
@staff_member_required
def system_settings(request):
    return render(request, 'accounts/system_settings.html')


# ✅ إدارة المستخدمين
@staff_member_required
def manage_users(request):
    return render(request, 'accounts/manage_users.html')


# ✅ التقارير
@staff_member_required
def reports(request):
    # هنا يجب أن تقوم بعرض صفحة التقارير
    return render(request, 'accounts/reports.html')

@login_required
def send_reminder(request):
    if request.method == 'POST':
        subject = '🔔 تذكير بالمهمة'
        message = 'مرحبًا، هذه رسالة تذكير لك بتنفيذ المهمة المحددة اليوم.'
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.success(request, '✅ تم إرسال التذكير إلى بريدك الإلكتروني.')
        except Exception as e:
            messages.error(request, f'❌ حدث خطأ أثناء الإرسال: {e}')
        return redirect('accounts:user_dashboard')  # الرجوع إلى صفحة لوحة التحكم

    return render(request, 'accounts/send_reminder.html')  # عرض صفحة تذكير

def system_settings(request):
    return render(request, 'accounts/system_settings.html')

def security_settings(request):
    # هنا يمكنك إضافة منطق إعدادات الأمان
    return render(request, 'accounts/security_settings.html')

def change_password(request):
    # هنا يتم منطق تغيير كلمة المرور
    return render(request, 'accounts/change_password.html')

def enable_2fa(request):
    # هنا يتم منطق تمكين التوثيق الثنائي
    return render(request, 'accounts/enable_2fa.html')

def active_sessions(request):
    # هنا يتم منطق عرض الجلسات النشطة
    return render(request, 'accounts/active_sessions.html')

def update_email(request):
    # هنا يتم منطق تحديث البريد الإلكتروني
    return render(request, 'accounts/update_email.html')

def general_settings(request):
    # هنا يمكنك إضافة منطق إعدادات النظام العامة
    return render(request, 'accounts/general_settings.html')