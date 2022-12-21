#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"ibots@ibots.com"}
cd /app/

python manage.py wait_for_db
python manage.py migrate
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true