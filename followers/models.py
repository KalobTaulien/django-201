from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    followed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    def __str__(self):
        return f"{self.followed_by.id} is following {self.following.id}"

    class Meta:
        unique_together = ('followed_by', 'following',)
