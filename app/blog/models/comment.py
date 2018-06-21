from django.db import models

from blog.models.post import Post
from members.models import InstagramUser


class Comment(models.Model):
    user = models.ForeignKey(
        InstagramUser,
        on_delete=models.CASCADE,
        related_name='my_comment',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def like_users(self):
        return self.comment_likes.all()

    def __str__(self):
        return f'{self.user}: {self.content}'




class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_likes',

    )
    user = models.ForeignKey(
        InstagramUser,
        on_delete=models.CASCADE,
        related_name = 'my_comment_likes',
    )