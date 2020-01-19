# Image
FROM python:3.8.1-buster

# Maintaner
MAINTAINER aniketrathore

# Unbuffered enviroment(console logs) for local develoment
ENV PYTHONUNBUFFERED 1

# Requirements
COPY requirements.txt .

# Requirments Intsall
RUN pip install -r requirements.txt

# Copying root file to working directory.
COPY ./app /app

# Setup Working Directorty
WORKDIR /app
