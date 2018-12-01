FROM nefarioustim/python:lxml-postgres

MAINTAINER Tim Huegdon <tim@timhuegdon.com>

ENV PIPENV_SHELL=/bin/bash
COPY . /app
WORKDIR /app
RUN apk add --update --no-cache --virtual=psql-client postgresql-client libffi-dev  &&\
    set -ex && pipenv install --dev --skip-lock                                     &&\
    rm -rf /root/.cache /var/cache /usr/share/terminfo
