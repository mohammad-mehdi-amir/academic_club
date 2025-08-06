
# Create your views here.
from rest_framework import viewsets, permissions
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrAdmin

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)