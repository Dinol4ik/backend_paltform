# Generated by Django 4.1.4 on 2023-04-24 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0009_section_themetask_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='themeTask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='subjects.themetask'),
        ),
    ]
