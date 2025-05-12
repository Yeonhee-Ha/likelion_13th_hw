from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def mypage(request):
    
    
    return render(request, 'users/mypage.html')