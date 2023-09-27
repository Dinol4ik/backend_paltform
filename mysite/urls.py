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

from apitest.views import CurseApi, SubjectApi, LessonApi, UserApi, ProfileApi, ProfileCurseApi, AddCurseInProfile, \
    subjectProfileApi, SectionTask, ThemeViewTask, Task, OnlyOneThemeTask, SolveTask, AllLessonInCourse, \
    SomeLessonInCourse, UserInCourse, CreateHomeWork, PopularCourse, TouchCourse, LessonsId

urlpatterns = [
                  path('api/v1/curses/', CurseApi.as_view()),
                  path('api/v1/curse/<int:pk>', TouchCourse.as_view()),
                  path('api/v1/lessonsInCourses/<int:pk>', AllLessonInCourse.as_view()),
                  path('api/v1/someLessonsInCourses/<int:pk>', SomeLessonInCourse.as_view()),
                  path('api/v1/subject/', SubjectApi.as_view()),
                  path('api/v1/lessons/', LessonApi.as_view()),
                  path('api/v1/zapiski/', ProfileCurseApi.as_view()),
                  path('api/v1/section/', SectionTask.as_view()),
                  path('api/v1/themeTask/', ThemeViewTask.as_view()),
                  path('api/v1/solveTaskInProfile/<int:profile_id>', SolveTask.as_view()),
                  path('api/v1/themeTask/<int:pk>', OnlyOneThemeTask.as_view()),
                  path('api/v1/UpdateHomeWork/<int:pk>', CreateHomeWork.as_view()),
                  path('api/v1/countBoughtCourses', PopularCourse.as_view()),
                  path('api/v1/task/', Task.as_view()),
                  path('api/v1/users/<int:pk>/', UserApi.as_view()),
                  path('api/v1/profile/<int:pk>/', ProfileApi.as_view()),
                  path('api/v1/subject/<int:pk>/', subjectProfileApi.as_view()),
                  path('api/v1/addcurse/', AddCurseInProfile.as_view()),
                    path('api/v1/getFutureLessons', LessonsId.as_view()),
                  # path('api/v1/popularCourse', PopularCourse.as_view()),
                  path('api/v1/userInCourse/<int:course_id>', UserInCourse.as_view()),
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('api/v1/drf-auth', include('rest_framework.urls')),
                  re_path(r'^auth/', include('djoser.urls')),  # auth в вконтакте - джосер
                  re_path(r'^auth/', include('djoser.urls.authtoken')),
                  re_path(r'^auth/', include('rest_framework_social_oauth2.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
