from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post,Blog

# Create your views here.
def mypage(request):
    
    user_blogs = Blog.objects.filter(writer=request.user)
    user_posts = Post.objects.filter(writer=request.user)
    
    return render(request, 'users/mypage.html', {'posts' : user_posts, 'blogs': user_blogs})