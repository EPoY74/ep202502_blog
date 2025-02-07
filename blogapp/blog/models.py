from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

    
class Post(models.Model):
    
    
    class Status(models.TextChoices):
        DRAFT='DF','Черновик'
        PUBLISHED='PB','Опублковано'
    
    
    title=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    
    body=models.TextField
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)


class Meta:
    ordering=['-publish']
    indexes=[
        models.Index(fields=['-publish']),
    ]
    verbose_name="Пост"
    verbose_name_plural="Посты"
    
def __str__(self):
    return self.title
    
