from django.db import models
from django.contrib.auth.models import User
from hullabaloo.settings import STATIC_URL

class Channel(models.Model):
    name  = models.CharField(max_length=50, verbose_name='channel name')
    def __unicode__(self):
        return self.name

class View(models.Model):
    user    = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)
    time    = models.DateTimeField(auto_now=True)

class Post(models.Model):
    image   = models.ImageField(upload_to=(STATIC_URL+"user/images/"),
                                height_field=None, width_field=None,
                                max_length=180, null=True, blank=True)
    body    = models.TextField(max_length=500, verbose_name='posts body')
    channel = models.ForeignKey(Channel)

    def __unicode__(self):
        return "Chan: " + self.channel.name + ", Body: " + self.body


