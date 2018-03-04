from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.views import PostViewSet
from comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]
