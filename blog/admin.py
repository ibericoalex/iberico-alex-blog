from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content',]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on',)
    search_fields = ['post', 'author', 'created_on',]
    list_filter = ('approved', 'created_on',)
    summernote_fields = ('body',)

# Register your models here.