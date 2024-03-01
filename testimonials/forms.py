from django import forms
from .models import Testimonials


class TestimonialForm(forms.ModelForm):
    """
    A form for creating new testimonials, based on the Testimonials model.
    """
    class Meta:
        model = Testimonials
        fields = ('content',)
