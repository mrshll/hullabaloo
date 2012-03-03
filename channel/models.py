from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=50, verbose_name='channel name')

    def __unicode__(self):
        return self.name

class Post(models.Model):
    body = models.TextField(max_length=500, verbose_name='posts body')
    channel = models.ForeignKey(Channel)

    def __unicode__(self):
        return "Chan: " + self.channel.name + ", Body: " + self.body


