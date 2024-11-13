#!/usr/bin/env bash

# Compile CSS
sass files/custom.scss files/style.css

# Django runserver
poetry run python manage.py runserver
