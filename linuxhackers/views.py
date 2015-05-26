from django.views.generic import *
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from linuxhackers.forms import *


class RecruitView(CreateView):
    template_name = 'recruit_create.html'
    form_class = RecruitForm
    success_url = 'thanks'


class RecruitDetailView(DetailView):
    template_name = 'recruit_detail.html'
    model = Recruit


class RecruitListView(ListView):
    template_name = 'recruit_list.html'
    queryset = Recruit.objects.all()
    context_object_name = 'recruit'


def recruit_login(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return redirect('/linuxhackers/recruit_list', None)
        #         return redirect('/newsfeed', None)
        #     else:
        #         return render_to_response('recruit_login.html', None)
        # else:
        #     return render_to_response('/join', None)
    return render_to_response('recruit_login.html', context_instance=RequestContext(request))