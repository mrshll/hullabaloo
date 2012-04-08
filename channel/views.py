from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.exceptions import MultipleObjectsReturned

import redis
import json
from channel.forms import NewForm
from channel.models import Post, Channel
from django.auth import User

@login_required
def show (request, channel_name):

    channel_name = channel_name.replace('%20',' ')
    print(channel_name)
    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})
    posts = Post.objects.filter(channel=channel.id)
    form = NewForm()
    return render_to_response('channel.html',
                {'form': form, 'posts': posts, 'channel': channel_name},
                context_instance=RequestContext(request))

@login_required
def new_post (request, channel_name):
    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})



