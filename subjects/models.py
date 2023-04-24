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
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    dateTime = models.DateTimeField('Дата и время занятия')

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
    themeTask = models.ForeignKey(ThemeTask, related_name='theme', on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=70)
    imgTask = models.ImageField('Фото Задание', upload_to='img/api/v1/task', blank=True)
    answer = models.FloatField('Ответ')

    def __str__(self):
        return self.title
