# urls.py (في المشروع الرئيسي)

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from core.views import home_page

# 🌐 مسارات عامة (غير خاضعة للغة)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/setlang/', set_language, name='set_language'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

# 🌐 المسارات التي تدعم اللغة (i18n)
urlpatterns += i18n_patterns(
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('management/', include('management.urls', namespace='management')),
    path('family/', include('family.urls')),
    path('calendar/', include('calendarhijri.urls')),
    path('sadaqa/', include('sadaqa.urls', namespace='sadaqa')),
    path('family/tasks/', include('family_tasks.urls', namespace='family_tasks')),
    path('family/expenses/', include('family_expenses.urls', namespace='family_expenses')),
    path('family/events/', include('family_events.urls', namespace='family_events')),
    path('family/notes/', include('family_notes.urls', namespace='family_notes')),
    path('', include('core.urls')),  # مسارات عامة إضافية
    prefix_default_language=True
)

# 🌐 ملفات static و media في وضع الإنتاج
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
