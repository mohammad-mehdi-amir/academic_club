from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleCreateSerializer
from accounts.permissions import IsMemberOrAdmin, IsAdmin

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-submitted_at')
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user, status='pending')

class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.AllowAny,)


from rest_framework.decorators import action, api_view, permission_classes
@api_view(['POST'])
@permission_classes([IsAdmin])
def article_change_status(request, pk):
    action = request.data.get('action')
    print(action)
    if action not in ('approve', 'reject'):
        return Response({'detail':'action must be approve or reject'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    article.status = 'approved' if action == 'approve' else 'rejected'
    article.save()
    return Response(ArticleSerializer(article).data)