
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('elearningplatform.urls')),

]
admin.site.site_header='CAN INSTITUTE ADMINISTRATION'
admin.site.site_title='CONTENT MANAGEMENT'


