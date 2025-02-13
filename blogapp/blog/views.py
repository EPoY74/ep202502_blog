# from django.http import Http404
from django.shortcuts import get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts':post})
# Create your views here.


def post_detail(request, post_id):
    post = get_object_or_404(Post,
                             id = post_id,
                             status = Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html', 
                  {'post':post})
