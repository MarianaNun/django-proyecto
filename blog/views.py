from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from datetime import datetime

# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {"posts": post}
    return render(request, 'index.html', context)

def crear_post(request):
    if request.POST:
        form= PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor= request.user
            post.fecha_creacion = datetime.now()
            post.save()
            return redirect('/blog')
    else:
        form= PostForm()
    return render(request, 'crear_post.html',  {"form": form})

def detalle_post(request, identificador):
    post = Post.objects.get(pk=identificador)
    context ={"post": post}
    return render(request, "detalle_post.html", context)


def editar_post(request, identificador):
    post = get_object_or_404(Post, pk=identificador)
    if request.POST:
        form= PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor= request.user
            post.fecha_creacion = datetime.now()
            post.save()
            return redirect('/blog')
    else:
        form= PostForm(instance= post)
    return render(request, 'editar_post.html',  {"form": form})

def eliminar_post(request, identificador):
    post = get_object_or_404(Post, pk=identificador)
    context = {"post": post}
    return render(request, "eliminar_post.html", context)

def confirmar_eliminacion(request, identificador):
    post= Post.objects.get(pk=identificador)
    post.delete()
    return redirect('/blog')

