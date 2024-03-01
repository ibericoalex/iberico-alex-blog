from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
]

"""
Defines URL patterns for the 'about' section of the website.
"""
