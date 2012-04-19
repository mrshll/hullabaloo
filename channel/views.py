from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.exceptions import MultipleObjectsReturned

import redis
import json
from datetime import datetime, timedelta
from channel.forms import NewForm
from channel.models import *

@login_required
def show (request, channel_name):
    print(channel_name)
    channel_name = channel_name.replace('-',' ')
    try:
        channel     = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})
    new_view, c = \
            View.objects.get_or_create(channel=channel, user=request.user)
    if not c:
        new_view.time = datetime.now()
    new_view.save()

    posts = Post.objects.filter(channel=channel.id)
    form = NewForm()
    return render_to_response('channel.html',
                {'form': NewForm(), 'posts': posts, 'channel': channel_name},
                context_instance=RequestContext(request))

@login_required
def new_post (request, channel_name):
    if request.method != 'POST':
        return render_to_response('error.html',
                {'error', 'non POST sent to channel.new_post'})

    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})

    #make a new post in the channel
    post = Post(channel=channel,
            body=request.POST['body'],
            image=request.FILES['image']);
    post.save()

    print(request.POST)

    #push new post to clients
    post_msg = {
          'channels': [channel.name],
          'data':     post.body,
          'image':    post.image.url,
    }
    r = redis.Redis()
    r.publish('juggernaut', json.dumps(post_msg))

    return HttpResponse('ok')

@login_required
def new_channel(request):
    if request.method != 'POST':
        return render_to_response('new_channel.html',
                    context_instance=RequestContext(request))
    else:
       channel_name = request.POST['name']
       channel, created = Channel.objects.get_or_create(name=channel_name)
       return HttpResponseRedirect("/channel/" + channel_name)

