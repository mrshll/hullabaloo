from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.exceptions import MultipleObjectsReturned

import redis
import json
from channel.forms import NewForm
from channel.models import Post, Channel

@login_required
def show (request, channel_name):
    print(channel_name)
    channel_name = channel_name.replace('-',' ')
    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})
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
            image=request.FILES['image']); #need to check if image is there
    post.save()

    print(request.POST)

    #push new post to clients
    post_msg = {
          'channels': [channel.name],
          'data': post.body
    }
    r = redis.Redis()
    r.publish('juggernaut', json.dumps(post_msg))

    return HttpResponse('ok')


