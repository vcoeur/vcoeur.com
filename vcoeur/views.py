from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.utils.translation import to_locale, get_language
from django.utils import translation
from django.conf import settings

from vcoeur.jinja2 import logger


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "home.html",
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
            articles=[
                dict(
                    slug='agile-of-course',
                    title='Agile? Yes of course! Wait… What is it?',
                    description='We all want to be Agile, but do we really know what it means?',
                ),
                dict(
                    slug='good-user-story',
                    title='We cannot define what a “Good User Story” is… And it does not matter',
                    description='What really matters about user stories',
                ),
                dict(
                    slug='low-cost-django-google',
                    title='Low-cost Django deployment with Google App Engine and Cloud SQL',
                    description='I was looking for a low-cost solution to deploy a basic Django app on Google Cloud',
                ),
            ],
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


def legal(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "legal.html",
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
