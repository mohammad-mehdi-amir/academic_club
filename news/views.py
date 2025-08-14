from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from accounts.permissions import IsMemberOrAdmin, IsAdmin

class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(status='published').order_by('-published_at')
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)

class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsMemberOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, status='draft')

class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.AllowAny,)

@api_view(['POST'])
@permission_classes([IsMemberOrAdmin])
def publish_news(request, pk):
    try:
        item = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    item.status = 'published'
    import django.utils.timezone as tz
    item.published_at = tz.now()
    item.save()
    return Response(NewsSerializer(item).data)