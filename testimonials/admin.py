from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonials

@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)