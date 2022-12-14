from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.auth),
    path('reg', views.reg, name='auth'),
    path('user', include('django.contrib.auth.urls')),
]