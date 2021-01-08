from django.contrib import admin
from .models import Follower


class FollowerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Follower, FollowerAdmin)
