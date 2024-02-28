from .models import Testimonials
from django import forms


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('content',)