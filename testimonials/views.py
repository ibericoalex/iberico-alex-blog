from django.shortcuts import render, reverse
from .models import Testimonials


def testimonials_list(request):
    """
    Renders the Testimonials page
    """
    testimonials = Testimonials.objects.all().order_by('-created_on') 

    return render(
        request,
        "testimonials/testimonials.html",
        {"testimonials": testimonials},
    )