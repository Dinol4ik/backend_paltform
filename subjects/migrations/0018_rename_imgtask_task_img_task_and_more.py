# Generated by Django 4.1.4 on 2023-05-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0017_rename_datetime_lesson_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='imgTask',
            new_name='img_task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='themeTask',
            new_name='theme_task',
        ),
    ]