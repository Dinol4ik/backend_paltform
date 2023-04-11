import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Profile, Enrollment
from .serializers import CurseSerializer, SubjectSerializer, LessonSerializer, UserSerializer, ProfileSerializer, \
    ProfileCurseSerializer, AddProfileCurse, SubjectInProfileSerializer
from subjects.models import Curse, subjects, Lesson


class CurseApi(generics.ListAPIView):
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
    permission_classes = (IsAuthenticated,) ##- ограничения на получение данных


class SubjectApi(generics.ListAPIView):
    queryset = subjects.objects.all()
    serializer_class = SubjectSerializer


class ProfileApi(generics.RetrieveAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer

class subjectProfileApi(generics.RetrieveAPIView):
    queryset = subjects.objects.all()
    serializer_class = SubjectInProfileSerializer


class ProfileCurseApi(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = ProfileCurseSerializer


class UserApi(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonApi(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AddCurseInProfile(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = AddProfileCurse

