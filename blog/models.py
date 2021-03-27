from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.title
