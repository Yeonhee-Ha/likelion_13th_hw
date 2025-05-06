from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
# Create your views here.

def mainpage(request):
    context = {
        'generation': 13,
        'info': {'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자화이팅!'},
        'shortKeys': [
            '들여쓰기: Tab',
            '내어쓰기: Shift + Tab',
            '주석처리: 윈도우-Ctrl + /, 맥-command + /',
            '자동정렬: Shift + Alt + F or Ctrl + K + F',
            '한줄이동: Alt + 방향키(위/아래)',
            '한줄삭제: Ctrl + Shift + k or Ctrl + x',
            '같은단어전체선택: Ctrl + Shift + L'
            ]
        }
    return render(request, 'main/mainpage.html',context)

def secondpage(request):
    blogs = Blog.objects.all()
    return render(request, 'main/secondpage.html', {'blogs': blogs})

def new_blog(request):
    return render(request, 'main/new-blog.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'main/detail.html', {'blog': blog})

def create(request):
    new_blog = Blog()
    
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.content = request.POST['content']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES.get('image')
    
    new_blog.save()
    
    return redirect('main:detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(pk=id)
    return render(request, 'main/edit.html', {"blog": edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(pk=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.content = request.POST['content']
    update_blog.pub_date = timezone.now()
    update_blog.image = request.FILES.get('image')
    
    update_blog.save()
    
    return redirect('main:detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(pk=id)
    delete_blog.delete()
    return redirect('main:secondpage')