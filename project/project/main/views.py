import re
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
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
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html', {'blogs': blogs, 'posts': posts})

def new_blog(request):
    return render(request, 'main/new-blog.html')

def new_post(request):
    return render(request, 'main/new-post.html')

#detail
def detail_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(blog=blog)
        return render(request, 'main/detail_blog.html', {'blog':blog, 'comments': comments})
    
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.blog = blog
        new_comment.writer=request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.post = None  # 또는 생략 가능

        new_comment.save()
        return redirect('main:detail_blog', id)
    
    return render(request, 'main/detail_blog.html', {'blog': blog})

def detail_post(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail_post.html', {'post':post, 'comments': comments})
    
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer=request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.blog = None

        new_comment.save()
        return redirect('main:detail_post', id)


    return render(request, 'main/detail_post.html', {'post': post })

#create
def create_blog(request):
    if request.user.is_authenticated:
        new_blog = Blog()
        
        new_blog.title = request.POST['title']
        new_blog.writer = request.user
        new_blog.content = request.POST['content']
        new_blog.pub_date = timezone.now()
        new_blog.image = request.FILES.get('image')
        
        new_blog.save()
        
        #본문을 띄어쓰기 기준으로 나누기
        pattern = r'\s+'   # r을 쓰면 백슬래시 1개만 써도 됨
        words = re.split(pattern, new_blog.content)
        tag_list = []
        
        # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:]) 
                #tag_list에 있는 Tag들을 new_blog의 tags에 추가
        for t in tag_list:
            #get_or_create() -> DB에 객체가 있다면 불러오고 없으면 만들어어
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_blog.tags.add(tag)
        

        return redirect('main:detail_blog', new_blog.id)
    
    else:
        return redirect('main:new_blog')  # 혹은 에러 처리


def create_post(request):
    if request.user.is_authenticated:
        new_post = Post()
        
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.content = request.POST['content']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')
        new_post.category = request.POST.get('category', '일반')
        
        new_post.save()

        #본문을 띄어쓰기 기준으로 나누기
        pattern = r'\s+'   # r을 쓰면 백슬래시 1개만 써도 됨
        words = re.split(pattern, new_post.content)
        tag_list = []
        
        # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:]) 
                #tag_list에 있는 Tag들을 new_blog의 tags에 추가
        for t in tag_list:
            #get_or_create() -> DB에 객체가 있다면 불러오고 없으면 만들어어
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag)


    
        return redirect('main:detail_post', new_post.id)
    
    else:
        return redirect('main:new_post')  # 혹은 에러 처리`

#edit
def edit_blog(request, id):
    edit_blog = Blog.objects.get(pk=id)
    return render(request, 'main/edit_blog.html', {"blog": edit_blog})

def edit_post(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit_post.html', {"post": edit_post})

#update
def update_blog(request, id):
    update_blog = Blog.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_blog.writer:
        update_blog.title = request.POST['title']
        update_blog.writer = request.user
        update_blog.content = request.POST['content']
        update_blog.pub_date = timezone.now()
        
        if request.FILES.get('image'):
            update_blog.image = request.FILES.get('image')
        update_blog.save()
        
        #본문을 띄어쓰기 기준으로 나누기
        pattern = r'\s+'   # r을 쓰면 백슬래시 1개만 써도 됨
        words = re.split(pattern, update_blog.content)
        tag_list = []
        
        # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:]) 
                #tag_list에 있는 Tag들을 new_blog의 tags에 추가
        
        for t in tag_list:
            #get_or_create() -> DB에 객체가 있다면 불러오고 없으면 만들어어
            tag, boolean = Tag.objects.get_or_create(name=t)
            update_blog.tags.add(tag)
        

        return redirect('main:detail_blog', update_blog.id)
    
    return redirect('accounts:login', update_blog.id)

def update_post(request, id):
    update_post = Post.objects.get(pk=id)

    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.writer = request.user
        update_post.category = request.POST.get('category', '일반')
        update_post.content = request.POST['content']
        update_post.pub_date = timezone.now()
        update_post.image = request.FILES.get('image')
        
        update_post.save()

        #본문을 띄어쓰기 기준으로 나누기
        pattern = r'\s+'   # r을 쓰면 백슬래시 1개만 써도 됨
        words = re.split(pattern, update_post.content)
        tag_list = []
        
        # 나눈 단어가 '#'으로 시작한다면 tag_list에 저장
        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:]) 
                #tag_list에 있는 Tag들을 new_blog의 tags에 추가
        for t in tag_list:
            #get_or_create() -> DB에 객체가 있다면 불러오고 없으면 만들어어
            tag, boolean = Tag.objects.get_or_create(name=t)
            update_post.tags.add(tag)
        
        return redirect('main:detail_post', update_post.id)
    return redirect('accounts:login', update_post.id)

#delete
def delete_blog(request, id):
    delete_blog = Blog.objects.get(pk=id)
    delete_blog.delete()
    return redirect('main:secondpage')

def delete_post(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:secondpage')


def tag_list(request):
#모든 태그 목록을 볼 수 있는 페이지
    tags= Tag.objects.all()
    return render(request, 'main/tag-list.html',{'tags': tags})

def tag_blogs(request, tag_id):#특정 태그를 가진 게시글의 목록을 볼 수 있는 페이지
    tag=get_object_or_404(Tag, id=tag_id)
    blogs=tag.blogs.all()
    return render(request, 'main/tag-blog.html',{
    'tag': tag,
    'blogs': blogs
    })

def tag_posts(request, tag_id):#특정 태그를 가진 게시글의 목록을 볼 수 있는 페이지
    tag=get_object_or_404(Tag, id=tag_id)
    posts=tag.posts.all()
    return render(request, 'main/tag-post.html',{
    'tag': tag,
    'posts': posts
    })

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    # 요청한 사용자가 댓글 작성자인지 확인
    if request.user == comment.writer:
        if comment.blog:  # 블로그 댓글이라면
            redirect_id = comment.blog.id
            comment.delete()
            return redirect('main:detail_blog', redirect_id)
        
        elif comment.post:  # 포스트 댓글이라면
            redirect_id = comment.post.id
            comment.delete()
            return redirect('main:detail_post', redirect_id)

def tag_redirect(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    if tag.blogs.exists():
        return redirect('main:tag-blogs', tag.id)
    elif tag.posts.exists():
        return redirect('main:tag-posts', tag.id)

def likes (request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.user in blog.like.all():
        blog.like.remove (request.user)
        blog.like_count -= 1
        blog.save()
    else:
        blog.like.add(request.user)
        blog.like_count += 1
        blog.save()
    return redirect('main:detail_blog', blog.id)

def likes_post (request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove (request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail_post', post.id)