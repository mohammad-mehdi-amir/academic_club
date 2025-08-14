from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleDetailView, article_change_status

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/status/', article_change_status, name='article-change-status'),
]