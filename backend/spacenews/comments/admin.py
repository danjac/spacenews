from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post', 'parent', )
    ordering = ('-created', )


admin.site.register(Comment, CommentAdmin)
