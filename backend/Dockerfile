FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y postgresql-client
ADD . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --dev
RUN pipenv run ./spacenews/manage.py migrate
