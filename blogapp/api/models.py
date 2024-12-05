import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogType(models.Model):
    blog_type_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    blog_type_name = models.CharField(null=False, max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_type_name


class Blogs(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog_title = models.CharField(null=False, max_length=256)
    blog_content = models.TextField()
    blog_type = models.ForeignKey(
        BlogType, on_delete=models.CASCADE, related_name="blog_type"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    created_on = models.DateTimeField(auto_now_add=True)
