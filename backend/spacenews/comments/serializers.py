from rest_framework import serializers

from accounts.serializers import UserSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment

        fields = (
            'id',
            'author',
            'post',
            'parent',
            'content',
            'created',
        )

        read_only_fields = (
            'post',
            'parent',
        )
