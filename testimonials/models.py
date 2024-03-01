from django.db import models
from django.contrib.auth.models import User
from django.db import models


STATUS = ((0, "Draft"), (1, "Published"))


class Testimonials(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="testimonials_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.author} wrote {self.content[:50]}"
