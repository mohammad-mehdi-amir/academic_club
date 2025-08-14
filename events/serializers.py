from rest_framework import serializers
from .models import Event, EventRegistration

class EventSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    registrations_count = serializers.IntegerField(source='registrations.count', read_only=True)

    class Meta:
        model = Event
        fields = ('id','title','description','date','capacity','created_by','created_by_username','created_at','registrations_count')

class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title','description','date','capacity')

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ('id','user','event','registered_at')
        read_only_fields = ('user','registered_at')