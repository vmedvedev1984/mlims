FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY django_app /django_app
WORKDIR /django_app
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password mlims-admin

USER mlims-admin
