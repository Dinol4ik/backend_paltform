from django.db import models
from django.contrib.auth.models import User
from subjects.models import Curse


class Profile(models.Model):
    name = models.CharField(max_length=70)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    curses = models.ManyToManyField(Curse, through='Enrollment')

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile.name
