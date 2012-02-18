from django.contrib import admin
from django.shortcuts import render_to_response
from posts.models import *

admin.autodiscover()

def home(request):
    posts = Post.objects.all()
    print(posts)
    return render_to_response('index.html', {'posts':posts})
