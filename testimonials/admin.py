from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonials

@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing testimonials with Summernote editor for the content field.
    """
    summernote_fields = ('content',)