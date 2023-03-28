from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('token', views.token),
    path('profile', views.profile, name='profile'),
    path('subj-url', views.subjectInAccount, name='subject_account')
]