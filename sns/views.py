from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from sns.forms import JoinForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext



def index(request):
    return render_to_response('index.html', None)

def newsfeed(request):
    return render_to_response('newsfeed.html', None)

class JoinView(CreateView):
    template_name = "join.html"
    model = User
    form_class = JoinForm
    success_url = "/"

def LoginTest(request):
    return render_to_response('login_test.html', None, context_instance=RequestContext(request))

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('index.html', None)
        else: return render_to_response('login.html', None)
    else: return  render_to_response('join.html', None)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def loginuser(request):
    username=None
    if request.user.is_authenticated():
        username = request.user.username
    else :
        username = "logout"
    return username
