from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'url',
            'description',
            'created',
        )
