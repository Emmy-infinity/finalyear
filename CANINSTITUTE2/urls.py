"""
URL configuration for CANINSTITUTE2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based vie
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('elearningplatform.urls'),
path('account/', include('django.contrib.auth.urls')),
]
admin.site.site_header='CAN INSTITUTE ADMINISTRATION'
admin.site.site_title='CONTENT MANAGEMENT'


