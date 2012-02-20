from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'hullabaloo.views.index', name='index'),
     url(r'^new/$', 'hullabaloo.views.new', name='new'),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()

