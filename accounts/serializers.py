from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'profile')
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if profile_data:
            Profile.objects.update_or_create(user=instance, defaults=profile_data)
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # role رو عمداً نمیذاریم

    def create(self, validated_data):

        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            role='user'  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user