from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .models import Comment
from .permissions import CommentPermission
from .serializers import CommentSerializer


class CommentViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    # we don't want to allow creating new comments, handled under posts

    queryset = Comment.objects.select_related('author').order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = (CommentPermission, )

    @detail_route(
        methods=['post'],
        permission_classes=[permissions.IsAuthenticated],
    )
    def reply(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        parent = self.get_object()

        serializer.save(
            parent=parent,
            post=parent.post,
            author=self.request.user,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
