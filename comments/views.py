from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        ct_id = self.request.query_params.get('content_type')
        obj_id = self.request.query_params.get('object_id')
        qs = Comment.objects.all()
        if ct_id and obj_id:
            qs = qs.filter(content_type_id=ct_id, object_id=obj_id)
        return qs

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)  

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.author != user and user.role != 'admin':
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You don't have permission to delete this comment")
        instance.delete()