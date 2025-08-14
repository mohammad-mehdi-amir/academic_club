from rest_framework import serializers
from .models import Comment
from django.contrib.contenttypes.models import ContentType

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id','author','author_username','content','created_at','content_type','object_id')
        read_only_fields = ('author','created_at')

    def validate(self, attrs):
        ct = attrs.get('content_type')
        if not ct:
            raise serializers.ValidationError({'content_type': 'required'})
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)