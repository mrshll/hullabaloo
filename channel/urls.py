from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('channel.views',
     url(r'^(?P<channel_name>[\w|\W]+)', 'show', name='show channel'),
     url(r'^(?P<channel_name>[\w|\W]+)/post/new', 'new_post', name='new post'),
)

