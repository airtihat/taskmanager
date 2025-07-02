from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# الأمان
SECRET_KEY = 'django-insecure-CHANGE_THIS_SECRET_KEY'
DEBUG = True
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'accounts',
    'tasks',
    'reports',
    'management',
    'pages',
    'family',
    'calendarhijri',
    'sadaqa',
    'family_tasks',
    'family_expenses',
    'family_events',
    'family_notes',
]

# نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.CustomUser'

# الوسطاء (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # تأكد من وجود هذا السطر
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف روابط المشروع
ROOT_URLCONF = 'taskmanager.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب الرئيسي
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'taskmanager.wsgi.application'

# إعدادات قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'  # يجب تغييره ليكون قابلًا للتغيير
TIME_ZONE = 'Asia/Riyadh'

# دعم الترجمة والتنسيقات المحلية
USE_I18N = True
USE_L10N = True  # لتفعيل التنسيق المحلي (التواريخ، الأرقام، إلخ)

# تحديد اسم ملف تعريف الارتباط للغة
LANGUAGE_COOKIE_NAME = 'django_language'

# اللغات المتاحة
LANGUAGES = [
    ('ar', 'العربية'),  # ❌ لا داعي لـ gettext_lazy هنا
    ('en', 'English'),
]

LANGUAGE_CODE = 'ar'  # أو 'en' حسب الحاجة

# موقع ملفات الترجمة
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# المسارات الثابتة والوسائط
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# الإعداد الافتراضي لمعرف الحقول
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# عند تسجيل الخروج
LOGOUT_REDIRECT_URL = '/'

# الإعدادات العامة
# عند محاولة الوصول لصفحة تتطلب تسجيل دخول
LOGIN_URL = '/accounts/login/'


SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 3600  # (مثال: الوقت بالثواني قبل انتهاء الجلسة)
