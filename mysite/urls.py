"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from apitest.views import CurseApi, SubjectApi, LessonApi, UserApi

urlpatterns = [
    path('api/v1/curses/', CurseApi.as_view()),
    path('api/v1/subject/', SubjectApi.as_view()),
    path('api/v1/lessons/', LessonApi.as_view()),
    path('api/v1/users/<int:pk>/', UserApi.as_view()),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/drf-auth', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls')),# auth в вконтакте - джосер
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
    path('subject/', include('subjects.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
