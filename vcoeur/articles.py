from __future__ import annotations

__all__ = [
    'articles',
]

good_user_story = dict(
    slug='good-user-story',
    title='We cannot define what a “Good User Story” is… And it does not matter',
    description='What really matters about user stories',
)

low_cost_django_google = dict(
    slug='low-cost-django-google',
    title='Low-cost Django deployment with Google App Engine and Cloud SQL',
    description='I was looking for a low-cost solution to deploy a basic Django app on Google Cloud',
)

agile_of_course = dict(
    slug='agile-of-course',
    title='Agile? Yes of course! Wait… What is it?',
    description='We all want to be Agile, but do we really know what it means?',
)

articles: list[dict] = [
    agile_of_course,
    good_user_story,
    low_cost_django_google,
]
