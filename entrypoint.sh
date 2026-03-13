#!/bin/sh
WIPE_DATA=${WIPE_DATA:-True}
echo "Waiting for database..."
while ! nc -z $DB_HOST 3306; do
  sleep 0.1
done
if [ "$WIPE_DATA" = "True" ]; then
  echo "Wiping data..."
  rm -rf /app/staticfiles/*
  python manage.py flush --noinput
fi
python manage.py clean_db
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py sync_users # This replaces the messy shell block
exec gunicorn --bind 0.0.0.0:8000 MikroLearning.wsgi:application