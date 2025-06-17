from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from main.models import Post, Blog

def mypage(request, id=None):
    # URL에 id가 없으면 로그인한 사용자의 마이페이지
    if id is None:
        user_profile = request.user
    else:
        user_profile = get_object_or_404(User, id=id)

    user_blogs = Blog.objects.filter(writer=user_profile)
    user_posts = Post.objects.filter(writer=user_profile)

    context = {
        'user_profile': user_profile,
        'blogs': user_blogs,
        'posts': user_posts,
    }
    return render(request, 'users/mypage.html', context)
