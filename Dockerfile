FROM python:3.8

ENV PYTHONDONTWRITERBYTECODE 1
ENV PYTHONUNBUFFERED 1 

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .