from django.db import models


class Post(models.Model):
    body=models.TextField(max_length=500, verbose_name='posts body')

class Channel(models.Model):
    name = models.CharField(max_length=50, verbose_name='channel name')
    posts = models.ManyToManyField(Post, blank=True)

    def __unicode__(self):
        return self.name
