from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import Post
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)
from django.views.generic import ListView
from .forms import EmailPostForm
from django.http import (HttpResponse,
                         HttpRequest)


def post_share(request:HttpRequest, post_id: int) -> HttpResponse:
    # Извлечь пост по идентификатору id
    post = get_object_or_404(Post,
                                id=post_id,
                                status=Post.Status.PUBLISHED)
    if request.method == "POST":
        # фОРМА БЫЛА ПЕРедана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            # ОТПРАВИТЬ электронное письмо
    else:
        form = EmailPostForm()
        
    return render(
        request,
        'blog/post/share.html',
        {
            'post':post,
            'form':form
        }
    )
        

class PostListView(ListView):
    """
    Альтернативное представлениесписка постов
    """
    queryset = Post.published.all()
    context_object_name='posts'
    paginate_by=3
    template_name='blog/post/list.html'


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
        
    except PageNotAnInteger:
        # Если номер страницы не int ,
        # то переходим на первую страницу
        posts = paginator.page(1)
        
    except EmptyPage:
        # Если страница находиться вне диапазона,
        # то выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})
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
