FROM nefarioustim/python:latest

MAINTAINER Tim Huegdon <tim@timhuegdon.com>

ENV PIPENV_SHELL=/bin/bash
COPY . /app
WORKDIR /app
