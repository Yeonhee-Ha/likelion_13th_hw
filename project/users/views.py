from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post,Blog


# Create your views here.
def mypage(request, id):
    
    user = get_object_or_404(User, pk=id)
    context = {
        'user': user,
        'user_blogs' : Blog.objects.filter(writer=user),
        'user_posts' : Post.objects.filter(writer=user),
    }
    return render(request, 'users/mypage.html', context)


def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)