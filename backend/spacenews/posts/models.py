from datetime import datetime

from django.conf import settings
from django.db import models


class Post(models.Model):

    author: settings.AUTH_USER_MODEL = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title: str = models.CharField(max_length=300)

    url: str = models.URLField(blank=True)
    description: str = models.TextField(blank=True)

    created: datetime = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
