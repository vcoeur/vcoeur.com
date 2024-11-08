#!/usr/bin/env bash

poetry export > requirements.txt
gcloud app deploy app-vcoeur.yaml dispatch.yaml --quiet
