#!/bin/bash

echo "Building Django project..."

cd backend

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate

echo "Build complete!"

