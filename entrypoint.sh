#!/bin/bash

python3 ./src/manage.py migrate --noinput

python3 ./src/manage.py loaddata clock_angles.json

python3 ./src/manage.py shell < ./src/utils/create_superuser.py

python3 ./src/manage.py runserver 0.0.0.0:8000
