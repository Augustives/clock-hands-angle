FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc

WORKDIR /src

COPY requirements.txt .

RUN pip install --upgrade pip && pip install psycopg2 && pip install -r requirements.txt --no-cache-dir

COPY . .
