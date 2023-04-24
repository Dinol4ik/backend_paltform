from django.contrib import admin
from .models import subjects, Curse, Lesson, Task, ThemeTask, Section
admin.site.register(subjects)
admin.site.register(Curse)
admin.site.register(Lesson)
admin.site.register(Task)
admin.site.register(ThemeTask)
admin.site.register(Section)

