from django.db import models  # pylint: disable=C0114
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):  # pylint: disable=C0115
    def get_queryset(self):  # pylint: disable=C0116
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):  # pylint: disable=C0115
    class Status(models.TextChoices):  # pylint: disable=C0115
        DRAFT='DF','Черновик'
        PUBLISHED='PB','Опублковано'


    title=models.CharField(max_length=255, unique=True, verbose_name='Заголовок')
    slug=models.SlugField(max_length=255, unique_for_date='publish', verbose_name='Слаг(путь)')
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
    objects = models.Manager()
    published = PublishedManager()


    class Meta:  # pylint: disable=C0115
        ordering=['-publish']
        indexes=[
            models.Index(fields=['publish']),
        ]
        verbose_name="Пост"
        verbose_name_plural="Посты"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):  # pylint: disable=C0116
        return reverse('blog:post_detail',
                        args=[self.id] # pylint: disable=E1101
                        #, так как поле создается автоматически
            )
