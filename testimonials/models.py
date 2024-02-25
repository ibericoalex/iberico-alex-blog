from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Testimonial(models.Model):
## _______________________________________NEED TO CHECK THE RELATED NAME - if it has to chanfe to testimonials_post
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="testimonials_posts"
)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Testimonial by {self.author}"


##_______________________________________WHAT TYPE IS AN AUTHOR VISUAL??
#    author_visual =

