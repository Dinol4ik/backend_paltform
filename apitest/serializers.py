from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Profile, Enrollment, TaskProfile
from subjects.models import Curse, subjects, Lesson, Section, Task, ThemeTask


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
        fields = ('profile', 'last_name', 'first_name', 'is_staff')


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


class CurseSerializerWithLesson(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Curse
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    curses = CurseSerializerWithLesson(many=True)

    # curses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = '__all__'


class AddProfileCurse(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class SubjectInProfileSerializer(serializers.ModelSerializer):
    curses = CurseSerializer(many=True)

    class Meta:
        model = subjects
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "img_task", "theme_task_id")


class ThemTaskSerializer(serializers.ModelSerializer):
    theme = TaskSerializer(many=True)

    class Meta:
        model = ThemeTask
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    section = ThemTaskSerializer(many=True)

    class Meta:
        model = Section
        fields = '__all__'


class SolveTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer()

    class Meta:
        model = TaskProfile
        fields = '__all__'


class CurseLessonSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Curse
        fields = '__all__'


class UserInCourseSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Enrollment
        fields = ('profile',)


class PopularCourseSerializer(serializers.ModelSerializer):
    course_count = serializers.IntegerField()

    class Meta:
        model = Enrollment
        fields = ('curse_id', 'course_count')


class CreateHomeWorkForCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id',)
