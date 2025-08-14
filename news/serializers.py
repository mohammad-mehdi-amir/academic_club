from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = News
        fields = ('id','title','content','created_by','created_by_username','status','created_at','published_at')
        read_only_fields = ('created_by','created_at','published_at','status')