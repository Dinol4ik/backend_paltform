from rest_framework import serializers

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

class LessonSerializer(serializers.ModelSerializer):
    curse = CurseSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'
