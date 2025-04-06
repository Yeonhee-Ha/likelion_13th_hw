from django.shortcuts import render

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
    return render(request, 'main/secondpage.html')

def week2page(request):
    return render(request, 'main/week2page.html')

def freepage(request):
    return render(request, 'main/freepage.html')