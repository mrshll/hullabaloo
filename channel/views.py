from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
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
    posts = Post.objects.filter(channel=channel.id)
    return render_to_response('channel.html',
                {'posts': posts, 'channel': channel_name})

@login_required
def new_post (request, channel_name):
    try:
        channel = Channel.objects.get(name=channel_name)
    except MultipleObjectsReturned:
        return render_to_response('error.html',
                {'error', 'multiple channels with name' + channel_name})



