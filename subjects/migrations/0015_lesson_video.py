# Generated by Django 4.1.4 on 2023-05-09 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0014_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, upload_to='video/api/v1/lesson'),
        ),
    ]