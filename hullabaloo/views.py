import socket
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from posts.forms import NewForm
from posts.models import *

import redis
import json

admin.autodiscover()

def index (request):
    posts = Post.objects.all()
    print(posts)
    return render_to_response('index.html', {'posts':posts})

def new (request):
    if request.POST:
        form = NewForm(request.POST)
        if form.is_valid():
            new_post = Post(body=request.POST['body'])
            new_post.save()
            push(new_post.body)
            print(new_post.body)
            return HttpResponseRedirect('/')
        return render_to_response('new.html')
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
    r.publish("jugernaut", json.dumps(msg))
    print( "Sent: {}".format(data) )

