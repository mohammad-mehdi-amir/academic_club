from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    submitted_by_username = serializers.CharField(source='submitted_by.username', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'submitted_by', 'submitted_by_username', 'status', 'submitted_at')
        read_only_fields = ('submitted_by', 'status', 'submitted_at')

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')