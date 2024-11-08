#!/usr/bin/env bash

poetry export > requirements.txt
gcloud app deploy app-test.yaml --quiet
#gcloud app deploy dispatch.yaml --quiet
