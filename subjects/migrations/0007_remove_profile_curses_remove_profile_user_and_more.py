# Generated by Django 4.1.4 on 2023-04-05 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_enrollment_profile_enrollment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='curses',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
