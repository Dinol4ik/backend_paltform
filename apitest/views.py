import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import CurseSerializer, SubjectSerializer, LessonSerializer, UserSerializer
from subjects.models import Curse, subjects, Lesson


class CurseApi(generics.ListAPIView):
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
    permission_classes = (IsAuthenticated,) ##- ограничения на получение данных


class SubjectApi(generics.ListAPIView):
    queryset = subjects.objects.all()
    serializer_class = SubjectSerializer

class UserApi(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonApi(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

