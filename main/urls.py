from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('token', views.token),
    path('analys', views.analysAnswer),
    path('api/statistic/<int:pk>', views.statistics),
    path('profile', views.profile, name='profile'),
    path('subj-url', views.subjectInAccount, name='subject_account'),
    path('take-live', views.check_live),
    path('test', views.order_by),
    path('chekUser', views.userInCourse),
    path('upload', views.file)
]
