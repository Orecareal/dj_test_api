from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.title} | {self.content} | on {self.created}"

    class Meta:
        verbose_name_plural = "Post"