from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post) перваяверсия.Сенйчасбудет расширенная

# выполняет ту же функцию, что и admin.site.register()  
@admin.register(Post)

# НАследуюсьоткласса, чтобы добавлять инфо, как 
# отображать модель и как с ней взаимодействовать
class PostAdmin(admin.ModelAdmin):
    
    # показываемполя модели которые мы хотим видеть в админке
    list_display=['title', 
    'slug',
    'author', 
    'publish',
    'status',]
