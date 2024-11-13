#!/usr/bin/env bash

# Export requirements
poetry export > requirements.txt

# Compile CSS
sass files/custom.scss files/style.css

# Collect static files
python manage.py collectstatic --clear --noinput

# Deploy to Google App Engine
gcloud app deploy app.yaml --quiet

