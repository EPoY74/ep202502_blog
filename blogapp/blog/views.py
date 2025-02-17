from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)
from django.views.generic import ListView
from .forms import EmailPostForm
from django.http import (HttpResponse,
                         HttpRequest)
from django.core.mail  import send_mail

from .models import Post


def post_share(request:HttpRequest, post_id: int) -> HttpResponse:
    # Извлечь пост по идентификатору id
    post = get_object_or_404(Post,
                                id=post_id,
                                status=Post.Status.PUBLISHED)
    sent:bool = False

    if request.method == "POST":
        # фОРМА БЫЛА ПЕРедана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            # ОТПРАВИТЬ электронное письмо
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} рекомендует тебе прочитать {post.title}"
            message = f"Прочитай {post.title} по адресу {post_url}/n/n{cd['name']} оставил комментарий: /n{cd['comments']}"
            
            send_mail(subject, message, 'epoy74@gmail.com', [cd['to']])
            sent=True
    else:
        form = EmailPostForm()
        
    return render(
        request,
        'blog/post/share.html',
        {
            'post':post,
            'form':form,
            'sent':sent
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
    all_post_list = Post.published.all()
    paginator = Paginator(all_post_list, 3)
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
