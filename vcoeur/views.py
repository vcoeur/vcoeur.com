from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.utils.translation import to_locale, get_language
from django.utils import translation
from django.conf import settings

from vcoeur.articles import articles
from vcoeur.jinja2 import logger


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        context=dict(
            active="index",
        ),
    )


def blog(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "blog.html",
        context=dict(
            active="blog",
            articles=articles,
        ),
    )

def article(request: HttpRequest, slug: str) -> HttpResponse:
    template_name = f"blog/articles/{slug}.html"
    try:
        return render(
            request,
            template_name=template_name,
            context=dict(
                active="blog",
            ),
        )
    except TemplateDoesNotExist:
        logger.error(f"Template {template_name} does not exist.")
        return redirect('blog')


def contact(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "contact.html",
        context=dict(
            active="contact",
        ),
    )


# EXTERNAL REDIRECT


def calendly(request: HttpRequest) -> HttpResponse:
    return redirect("https://calendly.com/vcoeur/contact")


# INTERNATIONALIZATION


def to_english(request: HttpRequest, path_from: str) -> HttpResponse:
    language = "en"
    translation.activate(language)
    response = redirect(path_from)
    # persist using the cookie
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


def to_french(request: HttpRequest, path_from: str) -> HttpResponse:
    language = "fr"
    translation.activate(language)
    response = redirect(path_from)
    # persist using the cookie
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
