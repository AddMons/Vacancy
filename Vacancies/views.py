from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all
    return render(request, 'Vacancies/post_list.html', {'posts': posts})

def home(request):
    return render(request, 'Vacancies/home.html',{})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Vacancies/detail.html',{'post': post})