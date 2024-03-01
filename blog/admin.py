from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing blog posts with
    Summernote editor for the content field.
    """
    list_display = ('title', 'status', 'created_on',)
    search_fields = ['title', 'content', ]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing comments on
    blog posts with Summernote editor for the body field.
    """
    list_display = ('post', 'author', 'approved', 'created_on',)
    search_fields = ['post', 'author', 'created_on', ]
    list_filter = ('approved', 'created_on',)
    summernote_fields = ('body',)
