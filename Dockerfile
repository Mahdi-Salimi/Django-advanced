FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y gcc

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app 

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt 

COPY ./core /app 

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
