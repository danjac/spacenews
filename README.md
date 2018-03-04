# spacenews
Django/Nuxt reference application

Overview
--------

This is an experiment in using NuxtJS (the SSR Vue framework) with Django as a backend.

Django Rest Framework is used to generate the API, with Djoser for auth endpoints (connecting to the NuxtJS auth-module on the frontend).

Both the NuxtJS application and Django API run behind nginx.

This is NOT a production ready application and bugs are to be expected.

Getting started
---------------

This setup requires Docker.

```
docker-compose up -d
docker-compose exec django bash
./spacenews/manage.py migrate
./spacenews/manage.py createsuperuser
```
