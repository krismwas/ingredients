FROM python:3.10.1-alpine3.14
MAINTAINER christopher

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user