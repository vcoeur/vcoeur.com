# v·coeur website

## Deploy with Cloud Run

Using Dockerfile and cloudbuild.yaml for automated build from GitHub main branch.

## Deploy with App Engine

Requires to generate the requirements.txt file, and to create an app.yaml.

````bash
poetry export > requirements.txt
gcloud app deploy
````

In order to dispatch domain names to services:
````bash
gcloud app deploy dispatch.yaml
````

## Compile

```
$ ./manage.py makemessages -a --no-obsolete
$ ./manage.py compilemessages
$ ./make-css.sh
$ ./manage.py collectstatic --no-input
```