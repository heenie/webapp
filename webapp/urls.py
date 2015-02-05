from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_change, password_change_done
from sns.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sns.views.index', name="index"),
    url(r'^join', JoinView.as_view(template_name="join.html"), name="join"),
    url(r'^write', WriteView.as_view(template_name="write.html"), name="write"),
    url(r'^article', ArticleView.as_view(template_name="article.html"), name="article"),
    url(r'^logintest', 'sns.views.LoginTest', name="test"),

    url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
    # url(r'^newsfeed', Newsfeed.as_view(template_name="newsfeed.html"), name="newsfeed"),
    # url(r'^newsfeed', ArticleView.as_view(template_name="newsfeed.html"), name="newsfeed"),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name="logout",),
    url(r'^password_change/$', password_change, {'template_name': 'password_change.html', 'post_change_redirect' :'/password_change/done/'}),
    url(r'^password_change/done', password_change_done, {'template_name': 'password_change_done.html'}),

)
# url(r'^login/$', 'django.contrib.auth.views.login'),
