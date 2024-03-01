from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating or editing a blog post comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)
