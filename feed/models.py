from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[0:100]
