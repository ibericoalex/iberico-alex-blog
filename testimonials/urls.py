from . import views
from django.urls import path

urlpatterns = [
    path('', views.testimonials_list, name='testimonials'),
]