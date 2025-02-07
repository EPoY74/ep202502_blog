from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    body=models.TextField
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


class Meta:
    ordering=['-publish']
    indexes=[
        models.Index(fields=['-publish'])
    ]
    verbose_name="Пост"
    verbose_name_plural="Посты"
    
def __str__(self):
    return self.title
    
