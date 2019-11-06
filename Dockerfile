FROM python:3.7
MAINTAINER jiaxin <edison7500@gmail.com>
RUN apt-get update && apt-get install -y supervisor
RUN mkdir  -p /data/www/
RUN git clone https://github.com/edison7500/manul.git /data/www/manul
WORKDIR /data/www/manul/
RUN pip install -r requirements/prod.txt


RUN echo "SECRET_KEY=$(cat /proc/sys/kernel/random/uuid)" >> .env
RUN echo "DJANGO_DEBUG=False" >> .env
RUN echo "DATABASE_URL=sqlite:///db.sqlite3" >> .env
RUN echo "DJANGO_LOG_FILE=/tmp/django.log" >> .env

RUN python manage.py migrate --settings="manul.settings.prod"
RUN python manage.py loaddata data.json --settings="manul.settings.prod"

COPY services/supervisor /etc/supervisor/conf.d/manul.conf
COPY services/gunicorn /etc/default/gunicon

EXPOSE 8000
CMD ["/usr/bin/supervisord"]
