FROM python:3.7
MAINTAINER jiaxin<edison7500@gmail.com>
RUN apt-get update && apt-get install -y supervisor
RUN mkdir  -p /data/www/
RUN git clone git@github.com:edison7500/manul.git /data/www/manul