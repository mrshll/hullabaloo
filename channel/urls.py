from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('channel.views',
     url(r'^(?P<channel_name>\w+)/$', 'show', name='show channel'),
     url(r'^(?P<channel_name>\w+)/post/new/$', 'new_post', name='new post'),
)

