#!/bin/sh
set -e


echo "Running migrations"
./manage.py migrate

echo "Current date $(date)}"



echo "Running management command!"


echo "Running the DJANGO WSGI server"
./manage.py runserver 0.0.0.0:8000

exec "$@"