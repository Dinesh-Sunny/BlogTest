from django.shortcuts import render, HttpResponse

from src.models import Post, Comment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'posts': posts, 'comments': comments})
