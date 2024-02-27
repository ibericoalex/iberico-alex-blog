from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))

class Testimonials(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="testimonials_posts"
)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.content[:50]  # Assuming you want to return the first 50 characters of the content