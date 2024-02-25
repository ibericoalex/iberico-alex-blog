from django.shortcuts import render
from django.views import generic
from .models import Testimonial

# Create your views here.
class TestimonialsList(generic.ListView):
    queryset = Testimonial.objects.all()
    template_name = "testimonial_list.html"