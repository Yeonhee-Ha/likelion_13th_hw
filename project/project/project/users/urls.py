from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
     path('mypage/<int:id>/', views.mypage, name='mypage-id'),  # 남의 마이페이지
]
