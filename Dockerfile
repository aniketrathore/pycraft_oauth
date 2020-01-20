# Image
FROM python:3.8.1-buster

# Maintainer
LABEL maintainer="Aniket Rathore <aniketrathore16@gmail.com>"

# Unbuffered enviroment(console logs) for local develoment
ENV PYTHONUNBUFFERED 1

# Copying requirements to image.
COPY requirements.txt requirements.txt

# Requirements install
RUN pip install -r requirements.txt

# Copying all root files to image.
COPY . .

# Setup working directory
WORKDIR /app

# Expose port for development server.
EXPOSE 8000

# Command to be run when container runs.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
