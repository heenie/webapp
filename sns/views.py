from django.contrib.auth.models import User
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView,  View, DetailView, ListView, DeleteView
from django.views.generic import *
from notifications import notify
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
        return context

    def get_list(self):
        articles = Article.objects.all().order_by('-datetime')
        array = []
        for article in articles:
            if Car.objects.filter(article=article).exists():
                array.append(Car.objects.get(article=article))
            elif House.objects.filter(article=article).exists():
                array.append(House.objects.get(article=article))
            elif Store.objects.filter(article=article).exists():
                array.append(Store.objects.get(article=article))
            else:
                array.append(article)
        return zip(articles, array)

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

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context.update({"article": Article.objects.get(id=self.kwargs['pk'])})
        return context

    def form_valid(self, form):
        form.instance.student = self.request.user.student
        form.instance.article = Article.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        article = form.instance.article
        content = form.instance.content
        verb = user.student.get_name() + '님이 회원님의 게시글에 댓글을 남겼습니다. ' + content
        # if user != article.student.user:
        notify.send(user, recipient=article.student.user, verb=verb)
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
        return context

    def get_list(self):
        articles = Article.objects.filter(student__id=self.kwargs['pk']).order_by('-datetime')
        array = []

        for article in articles:
            if Car.objects.filter(article=article).exists():
                array.append(Car.objects.get(article=article))
            elif House.objects.filter(article=article).exists():
                array.append(House.objects.get(article=article))
            elif Store.objects.filter(article=article).exists():
                array.append(Store.objects.get(article=article))
            else:
                array.append(article)
        return zip(articles, array)

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


class WriteDefaultView(CreateView):
    template_name = "write_default.html"
    form_class = WriteForm
    doc_form_class = DocumentForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        doc_form = self.doc_form_class()
        return render(request, self.template_name, {'form': form, 'doc': doc_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        doc_form = self.doc_form_class(request.POST, request.FILES)
        if doc_form.is_valid():
            article = form.save(commit=False)
            article.student = request.user.student
            article.category = Category.objects.get(name="기타")
            article.save()
            for file in request.FILES.getlist('docfile'):
                file = Image(image=file, article=article)
                file.save()
            return redirect('/newsfeed')
        return render_to_response(self.template_name, {'form': form, 'doc': doc_form}, context_instance=RequestContext(request))


class WriteCarView(CreateView):
    template_name = "write_car.html"
    form_class = WriteForm
    doc_form_class = DocumentForm
    trade_form_class = TradeForm
    extra_form_class = CarForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.type = "car"
        doc_form = self.doc_form_class()
        trade_form = self.trade_form_class()
        extra_form = self.extra_form_class()
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'trade': trade_form, 'car': extra_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        doc_form = self.doc_form_class(request.POST, request.FILES)
        trade_form = self.trade_form_class(request.POST)
        extra_form = self.extra_form_class(request.POST)
        if form.is_valid() and trade_form.is_valid() and extra_form.is_valid():
            article = form.save(commit=False)
            article.student = self.request.user.student
            article.category = Category.objects.get(type="car")
            article.save()
            for file in request.FILES.getlist('docfile'):
                file = Image(image=file, article=article)
                file.save()
            return redirect('/newsfeed')
            trade = trade_form.save(commit=False)
            trade.save()
            extra = extra_form.save(commit=False)
            extra.trade = trade
            extra.article = article
            extra.save()
            return redirect('newsfeed')
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'trade': trade_form, 'car': extra_form})


class WriteHouseView(CreateView):
    template_name = "write_house.html"
    form_class = WriteForm
    doc_form_class = DocumentForm
    extra_form_class = HouseForm
    success_url = "/newsfeed"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.type = "house"
        doc_form = self.doc_form_class()
        extra_form = self.extra_form_class()
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'house': extra_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        doc_form = self.doc_form_class(request.POST, request.FILES)
        extra_form = self.extra_form_class(request.POST)
        if form.is_valid() and extra_form.is_valid():
            article = form.save(commit=False)
            article.student = self.request.user.student
            article.category = Category.objects.get(type="house")
            article.save()
            for file in request.FILES.getlist('docfile'):
                file = Image(image=file, article=article)
                file.save()
            return redirect('/newsfeed')
            extra = extra_form.save(commit=False)
            extra.article = article
            extra.save()
            return redirect('newsfeed')
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'house': extra_form})


class WriteStoreView(CreateView):
    template_name = "write_store.html"
    form_class = WriteForm
    doc_form_class = DocumentForm
    trade_form_class = TradeForm
    extra_form_class = StoreForm
    success_url = "/newsfeed"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.type = "store"
        doc_form = self.doc_form_class()
        trade_form = self.trade_form_class()
        extra_form = self.extra_form_class()
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'trade': trade_form, 'store': extra_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        doc_form = self.doc_form_class(request.POST, request.FILES)
        trade_form = self.trade_form_class(request.POST)
        extra_form = self.extra_form_class(request.POST)
        if form.is_valid() and trade_form.is_valid() and extra_form.is_valid():
            article = form.save(commit=False)
            article.student = self.request.user.student
            article.category = Category.objects.get(type="store")
            article.save()
            for file in request.FILES.getlist('docfile'):
                file = Image(image=file, article=article)
                file.save()
            return redirect('/newsfeed')
            trade = trade_form.save(commit=False)
            trade.save()
            extra = extra_form.save(commit=False)
            extra.trade = trade
            extra.article = article
            extra.save()
            return redirect('newsfeed')
        return render(request, self.template_name, {'form': form, 'doc': doc_form, 'trade': trade_form, 'store': extra_form})


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