# Generated by Django 4.1.4 on 2023-02-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_curse_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='curse',
            name='information',
            field=models.TextField(default=2, verbose_name='Информация о курсе '),
            preserve_default=False,
        ),
    ]