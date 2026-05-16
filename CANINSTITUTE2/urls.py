from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('elearningplatform.urls')),
    path('account', include('django.contrib.auth.urls')),
    path('favicon.ico', TemplateView.as_view(template_name='favicon.ico', content_type='image/x-icon')),
]

# Serve static files and media files in production
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'CAN INSTITUTE ADMINISTRATION'
admin.site.site_title = 'CONTENT MANAGEMENT'
