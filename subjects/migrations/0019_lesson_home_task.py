# Generated by Django 4.1.4 on 2023-05-15 15:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0018_rename_imgtask_task_img_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='home_task',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
            preserve_default=False,
        ),
    ]