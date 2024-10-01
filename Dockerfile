FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libmariadb-dev default-libmysqlclient-dev pkg-config

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /app/

