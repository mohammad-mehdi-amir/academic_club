from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    submitted_by = serializers.ReadOnlyField(source='submitted_by.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'submitted_by', 'status', 'submitted_at']
        read_only_fields = ['submitted_by', 'status', 'submitted_at']