from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Profile
from subjects.models import Curse, subjects, Lesson




class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = ('id', 'title')

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = ()


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
