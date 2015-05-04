from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sns.views import *
from django.contrib.auth.views import login, logout, password_change, password_change_done
from webapp import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sns.views.index', name="index"),
    url(r'^join', JoinView.as_view(template_name="join.html"), name="join"),
    url(r'^write/(?P<type>\w+)', WriteView.as_view(), name="write"),
    url(r'^mypage/(?P<pk>\d+)$', MyPage.as_view(template_name="mypage.html"), name="mypage"),
    url(r'^article/(?P<pk>\d+)$', ArticleView.as_view(), name="article"),
    url(r'^comment-delete/(?P<comment_id>\d+)$', 'sns.views.comment_del', name="comment-delete"),
    url(r'^logintest', 'sns.views.LoginTest', name="test"),
    url(r'^login/$', login, {'template_name': 'login.html'}, name="login"),
    url(r'^newsfeed', Newsfeed.as_view(template_name="newsfeed.html"), name="newsfeed"),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name="logout",),
    url(r'^password_change/$', password_change, {'template_name': 'password_change.html', 'post_change_redirect' :'/password_change/done/'}),
    url(r'^password_change/done', password_change_done, {'template_name': 'password_change_done.html'}, name="personal"),
    # url(r'^personal_change', PersonalView.as_view(template_name="personal_change.html")),
    # url(r'^password_change/done', password_change_done, {'template_name': 'password_change_done.html'}),
    url(r'^setting/(?P<pk>\d+)$', SettingView.as_view(), name="setting"),
    url(r'^swipe/(?P<pk>\d+)$', SwipeView.as_view(), name="swipe"),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
