from .models import User
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def post_list(request):
    posts = User.objects.filter()
    return render(request, 'templates/registration/signup.html', {'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserForm()
    return render(request, 'templates/registration/signup.html', {'form': form})

