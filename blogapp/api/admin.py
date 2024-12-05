from django.contrib import admin
from .models import Blogs, BlogType

# Register your models here.
admin.site.register(BlogType)
admin.site.register(Blogs)
