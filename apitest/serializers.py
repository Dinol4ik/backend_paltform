from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Profile,Enrollment
from subjects.models import Curse, subjects, Lesson


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = ('id', 'title')


class CurseSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    class Meta:
        model = Curse
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = User
        # fields = ('first_name', 'last_name')
        fields = ('profile', 'last_name', 'first_name')

class LessonSerializer(serializers.ModelSerializer):
    curse = CurseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'


class ProfileCurseSerializer(serializers.ModelSerializer):
    curse = CurseSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = ('curse_id', 'profile_id', 'curse', 'date')


class ProfileSerializer(serializers.ModelSerializer):
    curses = CurseSerializer(many=True)
    # curses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = '__all__'




class AddProfileCurse(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class SubjectInProfileSerializer(serializers.ModelSerializer):
    curses = serializers.StringRelatedField(many=True)
    class Meta:
        model = subjects
        fields = '__all__'