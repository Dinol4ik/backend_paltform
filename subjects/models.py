from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class subjects(models.Model):
    title = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.title


class Curse(models.Model):
    subject = models.ForeignKey(subjects, related_name='curses', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    about = models.TextField('О курсе')
    information = models.TextField('Информация о курсе ')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    curse = models.ForeignKey(Curse, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    date_time = models.DateTimeField('Дата и время занятия')
    video = models.FileField(upload_to='video/api/v1/lesson', blank=True)
    home_task = ArrayField(models.CharField(max_length=100), blank=True)
    stream_status = models.CharField('Статус трансляции', max_length=50, default='offline')

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField('Номер задания', max_length=90)

    def __str__(self):
        return self.title


class ThemeTask(models.Model):
    section = models.ForeignKey(Section, related_name='section', on_delete=models.CASCADE)
    title = models.CharField('Тема заданий', max_length=90)

    def __str__(self):
        return self.title


class Task(models.Model):
    theme_task = models.ForeignKey(ThemeTask, related_name='theme', on_delete=models.CASCADE)
    title = models.TextField('Название')
    img_task = models.ImageField('Фото Задание', upload_to='img/api/v1/task', blank=True)
    answer = models.FloatField('Ответ')

    def __str__(self):
        return self.title
