from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
from sns.views import JoinView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sns.views.index', name="index"),
    url(r'^join', JoinView.as_view(template_name="join.html"), name="join"),

    url(r'^login/$', login, {'template_name': 'login.html'}, name="web-login"),
)
