from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from hullabaloo import settings

admin.autodiscover()

urlpatterns = patterns('',

    # our routes
    url(r'^$', 'hullabaloo.views.index', name='index'),
    url(r'^new/$', 'hullabaloo.views.new', name='new'),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^home/', 'hullabaloo.views.home'),

    # plugin routes
    url(r'^accounts/', include('registration.urls')),

    # static/media routes
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT}),

    # admin routes
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

