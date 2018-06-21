from django.contrib import admin

from blog.models.post import Post, PostLike
from blog.models.comment import Comment, CommentLike

admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
