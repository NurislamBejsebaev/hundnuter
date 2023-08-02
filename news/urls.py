from django.urls import path
from news.views import *

urlpatterns = [
    path('list-class-generic/', ArticleNewListView.as_view(), name='news-list-class-generic'),
    path('create/', ArticleNewCreateView.as_view(), name='news-create'),
    path('update/<int:pk>/', ArticleNewUpdateView.as_view(), name='news-update'),
    path('detail/<int:pk>/', news_detail, name='news-detail'),
]