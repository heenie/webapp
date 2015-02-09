from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import  reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, View, DetailView, ListView
from sns.admin import ArticleModelAdmin
from sns.filters import ArticleFilter
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


class Newsfeed(ListView):
    template_name = "newsfeed.html"
    queryset = Article.objects.all()
    context_object_name = "articles"
    

    def get_context_data(self, **kwargs):
        context = super(Newsfeed, self).get_context_data(**kwargs)
        context.update({"search_form": SearchForm(self.request.GET)})
        return context

    def get_queryset(self):
        category_param = self.request.GET.get('category')
        content_param = self.request.GET.get('content')

        articles = ArticleModelAdmin(Article, None).get_search_results(self.request, self.queryset, content_param)[0]
        articles = ArticleFilter(self.request.GET, queryset=articles)

        return articles

    def listing(request):
        articles = Article.objects.all();

        return render_to_response('newsfeed.html', {"articles": articles})


class JoinView(CreateView):
    template_name = "join.html"
    model = User
    form_class = JoinForm
    success_url = "/"


class WriteView(CreateView):
    template_name = "write.html"
    model = Article
    form_class = WriteForm
    success_url = "/newsfeed"

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        return super(WriteView, self).form_valid(form)



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
