from django.db import models

__all__ = (
    'InstagramUser',

)


class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    friends= models.ManyToManyField('self',
                                    symmetrical=False,
                                    related_name='my_friends',
                                    blank=True)
    block_users = models.ManyToManyField('self',
                                         symmetrical=False,
                                         related_name='block_friends',
                                         blank=True)

    @property
    def posts(self):
        return f'내가 작성한 글 목록: {self.post_set.all()}'

    @property
    def comments(self):
        return f'내가 작성한 댓글 목록: {self.my_comment.all()}'


    def __str__(self):
        return self.name


