from django.urls import path

from . import views

# Устанавливаем пространство имён приложения для идентификации URL-шаблонов
app_name = 'blog'

# Определяем URL-шаблоны для приложения "blog"
urlpatterns = [
    # URL-шаблон для главной страницы блога
    path('', views.index, name='index'),
    # URL-шаблон для страницы с деталями конкретного поста
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    # URL-шаблон для страницы с постами определённой категории
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
