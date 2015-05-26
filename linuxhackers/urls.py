from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from webapp import settings
from linuxhackers.views import *

urlpatterns = patterns('linuxhackers.views',
    url(r'^$', RecruitView.as_view(), name="linuxhackers"),
    url(r'^thanks$', TemplateView.as_view(template_name='thanks.html'), name="thanks"),
    url(r'^recruit_detail/(?P<pk>\d+)$', RecruitDetailView.as_view(), name="recruit-detail"),
    url(r'^recruit_list$', RecruitListView.as_view(), name="recruit-list"),
    url(r'^recruit_login/$', 'recruit_login', name="recruit-login"),
)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)