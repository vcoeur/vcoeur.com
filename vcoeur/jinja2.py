import logging

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from jinja2 import Environment

logger = logging.getLogger(__name__)


def _url(view_name: str, *args, **kwargs) -> str:
    return reverse(view_name, args=args, kwargs=kwargs)


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        url=_url,
        static=staticfiles_storage.url,
        settings=settings,
        _=_,
    )
    env.filters.update(
    )
    return env
