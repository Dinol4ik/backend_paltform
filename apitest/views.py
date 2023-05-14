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
    ThemTaskSerializer, SolveTaskSerializer, CurseLessonSerializer, UserInCourseSerializer
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
    serializer_class = SolveTaskSerializer

    def get_queryset(self):
        profile_id = self.kwargs['profile_id']
        return TaskProfile.objects.filter(profile=profile_id)


class AllLessonInCourse(generics.RetrieveAPIView):
    queryset = Curse.objects.all()
    serializer_class = CurseLessonSerializer


class SomeLessonInCourse(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class UserInCourse(generics.ListAPIView):
    serializer_class = UserInCourseSerializer

    def get_queryset(self):
        curse_id = self.kwargs['course_id']
        return Enrollment.objects.filter(curse_id=curse_id)
