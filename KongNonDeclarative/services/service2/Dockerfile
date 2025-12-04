FROM python:3.12-slim

WORKDIR /usr/src/core

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

