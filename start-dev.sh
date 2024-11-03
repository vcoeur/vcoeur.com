#!/usr/bin/env bash

./make-css.sh

poetry run python manage.py runserver
