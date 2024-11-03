#!/usr/bin/env bash

BASEDIR=$(dirname "$BASH_SOURCE")
export PYTHONPATH=$PYTHONPATH:$BASEDIR
exec /usr/bin/env gunicorn vcoeur.wsgi -b 0.0.0.0:8080 \
  --preload --worker-class gthread --workers 4 --threads 4 \
  --max-requests 1000 --max-requests-jitter 100 --timeout 30
