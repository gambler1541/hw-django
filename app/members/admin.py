from django.contrib import admin

from members.models import InstagramUser, UserInfo

admin.site.register(InstagramUser)
admin.site.register(UserInfo)
