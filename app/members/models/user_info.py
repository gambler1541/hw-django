from django.db import models

from .bloguser import InstagramUser
__all__=(
    'UserInfo',
)

class UserInfo(models.Model):
    user = models.OneToOneField(
        InstagramUser,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=80)

    def __str__(self):
        return '{}, {}, {}'.format(
            self.user,
            self.address,
            self.phone_number,
        )