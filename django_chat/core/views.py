from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def index(request):
    return render(request, 'core/index.html')

def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('yeah!!')
            return redirect('index')
        else:
            print('joder')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'core/signup.html', context)