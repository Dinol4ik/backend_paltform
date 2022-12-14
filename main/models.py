from django.db import models
from django.contrib.auth.models import User
from subjects.models import Curse


class Profile(models.Model):
    name = models.CharField(max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    curses = models.ManyToManyField(Curse, related_name='profiles')

    def __str__(self):
        return self.name
