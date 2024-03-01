from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Testimonials


@admin.register(Testimonials)
class TestimonialsAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing testimonials with
    Summernote editor for the content field.
    """
    list_display = ('truncated_content', 'author', 'status', 'created_on',)
    summernote_fields = ('content',)

    def truncated_content(self, obj):
        """
        Returns the first 80 characters of the testimonial
        content for display in the admin list.
        """
        return obj.content[
            :80] + '...' if len(obj.content) > 80 else obj.content
    truncated_content.short_description = 'Content'
    