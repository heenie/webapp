from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, View, DetailView
from sns.forms import JoinForm, WriteForm, ArticleForm
from sns.models import Article
from sns.forms import JoinForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from sns.models import Article


def index(request):
    return render_to_response('index.html', None)


# def newsfeed(request):
#     return render_to_response('newsfeed.html', None)


class Newsfeed(CreateView):
    template_name = "newsfeed.html"
    model = Article
    form_class = SearchForm


    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})


class JoinView(CreateView):
    template_name = "join.html"
    model = User
    form_class = JoinForm
    success_url = "/"


def search(request):
    return render_to_response('newsfeed.html', None)

# class SearchView(CreateView):
#     template_name = "search.html"
#     model = Article
#     form_class = SearchForm
#     success_url = "/"

def ArticleView(request):
    # template_name = "article.html"
    # model = Article
    # form_class = ArticleForm
    return render_to_response('article.html', None)


class WriteView(CreateView):
    template_name = "write.html"
    model = Article
    form_class = WriteForm
    success_url = "/"


def LoginTest(request):
    return render_to_response('login_test.html', None, context_instance=RequestContext(request))


def password_change(request):
    return render_to_response('password_change.html', None)


def password_change_done(request):
    return render_to_response('password_change_done.html', None)


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
