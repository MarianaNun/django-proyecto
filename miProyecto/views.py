from django.shortcuts import render, redirect
from blog.models import Post
from _datetime import datetime


def index(request):
    post = Post.objects.all()

    context = {"lista_de_alumnos": {"comision 1": ["Ana", "Camilo", "Adriana", "Pedro"],
                                    "comision 2": ["Francisco", "Andres", "Julia"],
                                    "comision 3": ["Hernan", "Paola", "Laura"]}}

    return render(request, 'index.html', context)


from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate


def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/blog')

    return render(request, "registro.html", {'form': form})


from django.contrib.auth import authenticate
def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                do_login(request, user)
                return redirect('/blog')

    return render(request, "login.html", {'form': form})


from django.contrib.auth import logout as do_logout
def logout(request):
    do_logout(request)
    return redirect('/blog')