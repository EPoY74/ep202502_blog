from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request,
                  {'blog/post/list.html'},
                  {'posts':post})
# Create your views here.

def post_detail(request, post_id):
    try:
        post = Post.published.get(id=post_id)
    except ObjectDoesNotExist as exc:
        print(f"{exc}")
        raise Http404("No post found") from exc

    return render(request,
                  'blog/post/detail.html', 
                  {'post':post})
