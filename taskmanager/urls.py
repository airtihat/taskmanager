from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from core.views import home_page

urlpatterns = [
    # تسجيل الخروج - مسار واحد فقط يجب أن يكون موجودًا
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    path('i18n/', include('django.conf.urls.i18n')),  # تغيير اللغة
    path('i18n/setlang/', set_language, name='set_language'),
]

# ✅ اللغة العربية تكون بدون /ar/
urlpatterns += i18n_patterns(
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('management/', include('management.urls', namespace='management')),
    prefix_default_language=False  # ✅ هذا السطر مهم
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
