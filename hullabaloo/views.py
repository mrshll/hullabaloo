import socket
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from channel.forms import NewForm
from channel.models import *

import redis
import json

admin.autodiscover()

def index (request):
    c = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    return render_to_response('index.html')

@login_required
def home (request):
    channel_list = Channel.objects.all()
    user_profile = request.user.get_profile()
    return render_to_response('home.html', {'user': request.user,
                                            'userprofile': user_profile,
                                            'channel_list': channel_list,
    }, context_instance=RequestContext(request))

def new_post (request):
    if request.POST:
        form = NewForm(request.POST)
        if form.is_valid():
            new_post = Post(body=request.POST['body'])
            new_post.save()
            push(new_post.body)
            print(new_post.body)
            return HttpResponse("Success")
    else:
        form = NewForm()
        data = {'form':form}
        csrfContext = RequestContext(request,data)
        return render_to_response('new.html', csrfContext)


def push (data):
#    HOST, PORT = "localhost", 9023
#    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock.sendto(data + "\n", (HOST, PORT))

    # juggernaut way
    post_msg = {
          "channels": ["test"],
          "data": data
    }
    r = redis.Redis()
    r.publish("juggernaut", json.dumps(post_msg))
    print( "Sent: {}".format(data) )

