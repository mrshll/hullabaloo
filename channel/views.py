from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

import redis
import json
from channel.models import Post


@login_required
def show (request, channel_name):
    posts = Post.objects.filter(channel__name=channel_name)
    return render_to_response('channel.html', {'posts': posts,
                                               'channel': channel_name})

@login_required
def new_post (request, channel_name):
    return render_to_response('home.html')