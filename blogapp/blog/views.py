from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts':post})
# Create your views here.


def post_detail(request, year:int, month:int, day:int, post:Post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html', 
                  {'post':post})
