from enum import Enum
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from environs import Env
from jinja2.filters import ignore_case

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = env.bool("DEBUG", default=False)

if DEBUG:
    SECRET_KEY = env.str(
        "SECRET_KEY",
        "django-insecure-%lu^t82tmd$kx=4%2^1(3c@v*cis1kjf21e8my)#*ih5ik@lb#",
    )
    ALLOWED_HOSTS = ["*"]
    CSRF_TRUSTED_ORIGINS = []
else:
    SECRET_KEY = env.str("SECRET_KEY")
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
    CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

ENVIRONMENT: str = env.enum(
    'ENVIRONMENT',
    type=Enum('ENVIRONMENT', 'DEBUG TEST PRODUCTION'),
    ignore_case=True,
    default='DEBUG',
).name

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "vcoeur",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vcoeur.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "vcoeur.jinja2.environment",
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "vcoeur.wsgi.application"

# Session in cookies
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "NAME": env.str("DATABASE_NAME", str(BASE_DIR / "db.sqlite3")),
        "USER": env.str("DATABASE_USER", ""),
        "PASSWORD": env.str("DATABASE_PASSWORD", ""),
        "HOST": env.str("DATABASE_HOST", ""),
        "PORT": env.str("DATABASE_PORT", ""),
        "CONN_MAX_AGE": env.int("DATABASE_CONN_MAX_AGE", 0),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGES = [
    ("fr", _("French")),
]

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "files",
]
STATIC_ROOT = BASE_DIR / "static"
# if not DEBUG:
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Site info
SITE_NAME = env.str("SITE_NAME", "vcoeur.com")
SITE_HOST_NAME = env.str("SITE_HOST_NAME", "")
SITE_HOST_SIREN = env.str("SITE_HOST_SIREN", "")
SITE_HOST_ADDRESS = env.str("SITE_HOST_ADDRESS", "")
