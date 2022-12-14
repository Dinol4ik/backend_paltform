from django import template

def unique(value):
    subjects = set()
    for course in value:
        subjects.add(course.subject)
    return subjects


register = template.Library()
register.filter('unique', unique)
