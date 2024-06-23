from django.urls import path
from .views import article_list, add_article, delete_article, chatbot, search, change_language

urlpatterns = [
    path('', article_list, name='article_list'),
    path('add/', add_article, name='add_article'),
    path('delete/<int:pk>/', delete_article, name='delete_article'),
    path('chatbot/', chatbot, name='chatbot'),
    path('search/', search, name='search'),
    path('change-language/<str:language>/', change_language, name='change_language'),
]
