import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Profile, Enrollment, TaskProfile
from .serializers import CurseSerializer, SubjectSerializer, LessonSerializer, UserSerializer, ProfileSerializer, \
    ProfileCurseSerializer, AddProfileCurse, SubjectInProfileSerializer, SectionSerializer, TaskSerializer, \
    ThemTaskSerializer, SolveTaskSerializer, CurseLessonSerializer
from subjects.models import Curse, subjects, Lesson, Section, Task, ThemeTask


class CurseApi(generics.ListAPIView):
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
    # permission_classes = (IsAuthenticated,) ##- ограничения на получение данных


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


class SectionTask(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ThemeViewTask(generics.ListAPIView):
    queryset = ThemeTask.objects.all()
    serializer_class = ThemTaskSerializer


class OnlyOneThemeTask(generics.RetrieveAPIView):
    queryset = ThemeTask.objects.all()
    serializer_class = ThemTaskSerializer


class Task(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SolveTask(generics.ListAPIView):
    lookup_field = "profile_id"
    queryset = TaskProfile.objects.filter()
    serializer_class = SolveTaskSerializer
    # def get(self, request, pk, **kwargs):
    #     b = TaskProfile.objects.filter(profile_id=pk).values()
    #     return self.retrieve(request, pk, **kwargs)
    # #     return Response({'test': list(b)})


class AllLessonInCourse(generics.RetrieveAPIView):
    queryset = Curse.objects.all()
    serializer_class = CurseLessonSerializer
