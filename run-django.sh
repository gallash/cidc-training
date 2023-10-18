#!/bin/sh

cd /code

python manage.py migrate --settings=project.settings_production
python manage.py runserver 0.0.0.0:8000 --settings=project.settings_production  # Exposing server 0.0.0.0
