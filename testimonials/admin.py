from django.contrib import admin
from .models import Testimonials
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)