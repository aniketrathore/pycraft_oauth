# Image
FROM python:3.8.1-buster

# Maintainer
LABEL maintainer="Aniket Rathore <aniketrathore16@gmail.com>"

# Unbuffered enviroment(console logs) for local develoment
ENV PYTHONUNBUFFERED 1

# Copying all root files to image.
COPY . .

# Requirements Install
RUN pip install -r requirements.txt

# Setup Working Directory
WORKDIR /app

# Expose port for development server.
EXPOSE 8000