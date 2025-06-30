from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, '❌ اسم المستخدم أو كلمة المرور غير صحيحة')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '✅ تم إنشاء الحساب بنجاح!')

            # إرسال بريد ترحيبي
            send_mail(
                subject='🎉 مرحبًا بك في نظام إدارة المهام',
                message='شكرًا لانضمامك. يمكنك الآن البدء في إدارة مهامك بكفاءة.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )

            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html', {
        'tasks_count': request.user.tasks.count() if hasattr(request.user, 'tasks') else 0,
    })


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


# ✅ ملف المستخدم الشخصي
@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user
    })

@staff_member_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})