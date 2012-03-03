from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

import redis
import json
from channel.models import Post, Channel


@login_required
def show (request, channel_name):
    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})
    posts = Post.objects.filter(channel__name=channel_name)
    return render_to_response('channel.html',
                {'posts': posts, 'channel': channel_name})
@login_required
def new_post (request, channel_name):
    return render_to_response('home.html')