from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from main.models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, last_name=instance.last_name, first_name=instance.first_name, name=instance.username)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
