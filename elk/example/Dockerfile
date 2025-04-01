FROM python:3.11-alpine AS base
WORKDIR /app
EXPOSE 8000

# Копируем исходный код
COPY ./ /app

RUN pip install fastapi[standard]
RUN pip install python-logstash-async
CMD ["fastapi", "run"]
