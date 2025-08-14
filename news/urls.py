
from django.urls import path
from .views import NewsListView, NewsCreateView, NewsDetailView, publish_news

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('create/', NewsCreateView.as_view(), name='news-create'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/publish/', publish_news, name='news-publish'),
]