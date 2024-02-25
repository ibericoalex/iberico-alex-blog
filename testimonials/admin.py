from django.contrib import admin
from .models import Testimonial
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Testimonial)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('content', 'status', 'created_on',)
    search_fields = ['content',]
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)

# Register your models here.