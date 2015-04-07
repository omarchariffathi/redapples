from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template import RequestContext, loader, TemplateDoesNotExist
from my_project import forms
#write your code below


def login(request):
    print request.POST
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def logged_in(request):
    print request.POST
    return render_to_response(
        'logged_in.html',
        {'full_name': request.user.username},
    )


def auth_view(request):
    print request.POST
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/g/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid_login(request):
    return render_to_response('invalid_login.html')


def register_user(request):
    if request.method == 'POST':
        print request.POST
        form = forms.UserCreateForm(request.POST)
        context = {"form": form}
        template = "register.html"
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = forms.UserCreateForm()
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')