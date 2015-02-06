from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView, View
from sns.forms import *
from sns.models import Article
from sns.forms import JoinForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from sns.models import Article


def index(request):
    return render_to_response('index.html', None)


class Newsfeed(CreateView):
    template_name = "newsfeed.html"
    # queryset = Article.objects.all()
    # context_object_name = "articles"
    form_class = SearchForm

    # def get_context_data(self, **kwargs):
    #     context = super(Newsfeed, self).get_context_data(**kwargs)
    #     context.update({"search_form": SearchForm(self.request.GET)})
    #     return context

class JoinView(CreateView):
    template_name = "join.html"
    model = User
    form_class = JoinForm
    success_url = "/"


class SearchView(View):
    template_name = "header.html"
    form_class = SearchForm
    success_url = "/"


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
