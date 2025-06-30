from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime

# ✅ الصفحة الرئيسية (عامّة)
def home_page(request):
    print("✅ تم استدعاء الصفحة الرئيسية")
    return render(request, 'core/home.html')  # قالب عام في templates/home.html

# ✅ لوحة تحكم المستخدم (تحتاج تسجيل دخول)
@login_required
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html')  # قالب المستخدم في accounts

# ✅ صفحة الإعدادات (تحتاج تسجيل دخول)
@login_required
def settings_view(request):
    context = {
        'year': datetime.datetime.now().year
    }
    return render(request, 'core/settings.html', context)  # قالب الإعدادات
