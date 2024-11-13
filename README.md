# vcoeur.com website source code

This project is [VCOEUR.COM](https://vcoeur.com) website source code.

## Run locally

You need to create `.env`, using `.env.example` as a template. In order to update the css, you can edit `files/custom.css`. 

You can then run the server with the following command (requires sass):

```bash
./runserver.sh
```


## Deploy with App Engine

You need to create a `app.yaml`, using `app.example.yaml` as a template.

You can deploy the app with the following commands:

```bash
deploy-app.sh
```


## Deploy with Heroku

The `Procfile` is provided.

