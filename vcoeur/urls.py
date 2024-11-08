from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from vcoeur import views

urlpatterns = [
    # Pages
    path("", views.home, name="index"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("blog/<str:slug>/", views.article, name="article"),
    path("legal/", views.legal, name="legal"),
    # Internationalization
    path("to-en/<path:path_from>", views.to_english, name="to_english"),
    path("to-fr/<path:path_from>", views.to_french, name="to_french"),
    # Calendly Redirect
    path("calendly/", views.calendly, name="calendly"),
]
 