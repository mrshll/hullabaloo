from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from hullabaloo import settings

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'hullabaloo.views.index', name='index'),
     url(r'^channel/$', include('channel.urls'))
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.STATIC_ROOT}),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),

     url(r'^admin/', include(admin.site.urls)),
)

