from django.urls import path
from django.views.generic import TemplateView

# Устанавливаем пространство имён приложения для идентификации URL-шаблонов
app_name = 'pages'

# Определяем URL-шаблоны для приложения "pages"
urlpatterns = [
    # URL-шаблон для страницы "О нас"
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # URL-шаблон для страницы "Правила"
    path('rules/', TemplateView.as_view(template_name='pages/rules.html'), name='rules'),
]