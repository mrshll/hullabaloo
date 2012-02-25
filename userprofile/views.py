from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def me(request):
    user = User.objects.get(id=request.user.id)
    return render_to_response("profile/view.html", context_instance=RequestContext(request, {"user":user}))

