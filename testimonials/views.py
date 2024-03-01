from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Testimonials
from .forms import TestimonialForm


def testimonials_list(request):
    """
    Renders the Testimonials page
    """
    testimonials = Testimonials.objects.filter(
        status=1).order_by('-created_on')
    testimonials_form = TestimonialForm()

    if request.method == "POST":
        testimonials_form = TestimonialForm(data=request.POST)
        if testimonials_form.is_valid():
            testimonials_form.instance.author = request.user
            testimonials_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Testimonial sent! Awaiting approval!")
        return HttpResponseRedirect(reverse('testimonials'))

    return render(
        request,
        "testimonials/index.html",
        {"testimonials": testimonials, "form": testimonials_form},
    )
