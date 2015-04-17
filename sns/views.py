from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,  View, DetailView, ListView, DeleteView
from django.views.generic import *
from sns.admin import ArticleModelAdmin
from sns.filters import ArticleFilter
from sns.forms import *
from sns.models import *
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', None)


class Newsfeed(ListView):
    template_name = "newsfeed.html"
    queryset = Article.objects.all()
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        context = super(Newsfeed, self).get_context_data(**kwargs)
        context.update({"search_form": SearchForm(self.request.GET)})
        context['get_list'] = get_lists(Article.objects.all().order_by('-datetime'))
        return context

    def get_queryset(self):
        category_param = self.request.GET.get('category')
        content_param = self.request.GET.get('content')

        articles = Article.objects.all().order_by('-datetime')
        articles = ArticleModelAdmin(Article, None).get_search_results(self.request, articles, content_param)[0]
        articles = ArticleFilter(self.request.GET, queryset=articles)
        return articles


class ArticleView(CreateView):
    template_name = "article_detail.html"
    model = Comment
    form_class = CommentForm

    def get_user_image(self):
        user = Student.objects.get(user=self.request.user)
        return user.get_image()

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        article = Article.objects.get(id=self.kwargs['pk'])
        context['article'] = article
        if Car.objects.filter(article=article).exists():
            context['board'] = Car.objects.get(article=article)
            self.template_name = 'article_detail_car.html'
        elif House.objects.filter(article=article).exists():
            context['board'] = House.objects.get(article=article)
            self.template_name = 'article_detail_house.html'
        elif Store.objects.filter(article=article).exists():
            context['board'] = Store.objects.get(article=article)
            self.template_name = 'article_detail_store.html'
        else:
            self.template_name = 'article_detail_default.html'
        return context

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        form.instance.article = Article.objects.get(id=self.kwargs['pk'])
        return super(ArticleView, self).form_valid(form)

    def get_success_url(self):
        return reverse('article', kwargs={'pk': self.kwargs['pk']})


class CommentDelete(DeleteView):
    template_name = "comment_delete.html"
    model = Comment
    success_url = "/newsfeed"   #todo 뒤로 기능 (+article.html에 있는 뒤로 버튼)


class SettingsView(UpdateView):
    template_name = "setting.html"
    model = User
    form_class = PersonalForm
    success_url = "/setting"
    #
    # def get_context_data(self, **kwargs):
    #     context = super(SettingsView, self).get_context_data()
    #     context.update({"student": Student.objects.get(id=self.kwargs['pk'])})
    #     return context


class SwipeView(ListView):
    context_object_name = 'imgs'

    def get_queryset(self):
        return Article.objects.get(id=self.kwargs['pk']).get_images()


def comment_del(request, comment_id):
    Comment.objects.filter(id=comment_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class JoinView(CreateView):
    template_name = "join.html"
    model = User
    form_class = JoinForm
    success_url = "/"


# class PersonalView(CreateView):
#     template_name = "personal_change.html"
#     model = User
#     form_class = PersonalForm
#     success_url = "/change"


class MyPage(ListView):
    template_name = "mypage.html"
    context_object_name = "my_articles"

    # def get(self, request, *args, **kwargs):
    #     student = Student.objects.get(id=kwargs['pk'])
    #     return render(request, self.template_name, {'student': student})

    def get_context_data(self, **kwargs):
        context = super(MyPage, self).get_context_data(**kwargs)
        context.update({"search_form": SearchForm(self.request.GET)})
        context.update({"student": Student.objects.get(id=self.kwargs['pk'])})
        context['get_list'] = get_lists(Article.objects.filter(student__id=self.kwargs['pk']).order_by('-datetime'))
        return context

    def get_queryset(self):
        category_param = self.request.GET.get('category')
        content_param = self.request.GET.get('content')

        articles = Article.objects.filter(student__id=self.kwargs['pk']).order_by('-datetime')
        # articles = Article.objects.filter(student=self.request.user.student).order_by('-datetime')
        articles = ArticleModelAdmin(Article, None).get_search_results(self.request, articles, content_param)[0]
        articles = ArticleFilter(self.request.GET, queryset=articles)
        return articles


class SettingView(UpdateView):
    template_name = "setting.html"
    model = User
    form_class = JoinForm
    success_url = "/newsfeed"


class WriteView(CreateView):
    template_name = 'write_default.html'
    form_class = WriteForm
    doc_form_class = DocumentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        doc_form = self.doc_form_class()

        forms = {'form': form, 'doc': doc_form}
        type = self.kwargs['type']
        form.type = type

        if type != 'default':
            self.template_name = 'write_' + type + '.html'
            form.type = type
            forms['trade'] = TradeForm()
            if type == 'car':
                forms['car'] = CarForm()
            elif type == 'house':
                forms['house'] = HouseForm()
            elif type == 'store':
                forms['store'] = StoreForm()
        return render(request, self.template_name, forms)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        doc_form = self.doc_form_class(request.POST, request.FILES)
        trade_form = None
        extra_form = None

        forms = {'form': form, 'doc': doc_form}
        type = self.kwargs['type']
        valid = doc_form.is_valid()

        if type != 'default':
            self.template_name = 'write_' + type + '.html'
            form.type = type
            trade_form = TradeForm(request.POST)
            forms['trade'] = trade_form
            if type == 'car':
                extra_form = CarForm(request.POST)
            elif type == 'house':
                extra_form = HouseForm(request.POST)
            elif type == 'store':
                extra_form = StoreForm(request.POST)
            forms[type] = extra_form
            valid = doc_form.is_valid() and trade_form.is_valid() and extra_form.is_valid()

        if valid:
            article = form.save(commit=False)
            article.student = self.request.user.student
            article.category = Category.objects.get(type=type)
            article.save()
            for file in request.FILES.getlist('docfile'):
                file = Image(image=file, article=article)
                file.save()
            if type != 'default':
                trade = trade_form.save(commit=False)
                trade.save()
                extra = extra_form.save(commit=False)
                extra.trade = trade
                extra.article = article
                extra.save()
            return redirect('newsfeed')
        return render_to_response(self.template_name, forms, context_instance=RequestContext(request))


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


def get_lists(articles):
    array = []
    for article in articles:
        list = {}
        if Car.objects.filter(article=article).exists():
            list['board'] = Car.objects.get(article=article)
            list['type'] = 'car'
        elif House.objects.filter(article=article).exists():
            list['board'] = House.objects.get(article=article)
            list['type'] = 'house'
        elif Store.objects.filter(article=article).exists():
            list['board'] = Store.objects.get(article=article)
            list['type'] = 'store'
        else:
            list['board'] = article
            list['type'] = 'default'
        array.append(list)
    return array