from django.urls import path
from . import views

app_name: str = 'blog'


urlpatterns = [
    # Представление поста
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail')
]