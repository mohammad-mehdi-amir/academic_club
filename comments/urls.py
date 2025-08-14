from django.urls import path
from .views import CommentListCreateView, CommentDeleteView

urlpatterns = [
    path('write/', CommentListCreateView.as_view(), name='comments-list-create'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]