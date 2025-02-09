from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT='DF','Черновик'
        PUBLISHED='PB','Опублковано'
    
    
    title=models.CharField(max_length=100, unique=True, verbose_name='Заголовок')
    slug=models.SlugField(max_length=100, unique=True, verbose_name='Слаг(путь)')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='Автор')

    body=models.TextField(verbose_name='Текст поста')
    publish=models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated=models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT,
                              verbose_name='Статус поста')

    class Meta:
        """"""
        ordering=['-publish']
        indexes=[
            models.Index(fields=['publish']),
        ]
        verbose_name="Пост"
        verbose_name_plural="Посты"

    def __str__(self):
        return str(self.title)

