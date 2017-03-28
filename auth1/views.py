from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html')


def home(request):
    fullname = request.user.username
    content = {'full_name': fullname}
    return render(request, 'home.html', content)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('logget')
    else:
        return HttpResponseRedirect('/invalid')


def logget(request):
    fullname = request.user.username
    content = {'full_name': fullname}
    return render_to_response('logget.html', content)


def invalid(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)


def register_success(request):
    fullname = request.user.username
    content = {'full_name': fullname}
    return render_to_response('register_success.html', content)
