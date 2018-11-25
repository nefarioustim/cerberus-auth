FROM nefarioustim/python:latest

MAINTAINER Tim Huegdon <tim@timhuegdon.com>

ENV PIPENV_SHELL=/bin/bash
COPY . /app
WORKDIR /app
RUN set -ex && pipenv install --dev --skip-lock         &&\
    rm -rf /root/.cache /var/cache /usr/share/terminfo
