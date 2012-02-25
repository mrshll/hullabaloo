__author__ = 'alden'

admin.autodiscover()

urlpatterns = patterns('channel.views',
     url(r'^$', 'index', name='show channel'),
     url(r'posts/$', index, name='show channel')
     url(r'^post/new/$', 'new_post', name='new post'),
)

