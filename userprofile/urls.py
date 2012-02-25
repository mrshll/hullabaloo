from django.conf.urls import *

urlpatterns = patterns('userprofile.views',
    url(r'^me/$', 'me'),
)