FROM python:3.10-alpine

RUN apk update && \
    apk add --no-cache --virtual postgresql-dev gcc python3-dev musl-dev

WORKDIR /app/

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn && pip install psycopg2-binary && pip install django==3.2.19

COPY . .
ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]
#FROM python:3.6
#
#COPY ./mysite /srv/www/<project>
#WORKDIR /srv/www/mysite
#
#RUN pip install -r requirements.txt