#!/bin/sh

python manage.py check && \
    python manage.py makemigrations && \
    python manage.py migrate --no-input
    gunicorn --config gunicorn.conf.py mysite.wsgi:application
