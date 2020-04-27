from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
from like import services as likes_services


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'author', 'title', 'content', 'created_at', 'is_fan', 'total_likes')
        model = Post

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')