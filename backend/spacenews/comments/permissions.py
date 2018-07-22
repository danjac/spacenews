from typing import Any

from django.views.generic import View

from rest_framework import permissions
from rest_framework.request import Request


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: View, obj: Any
    ) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return obj.author == request.user
