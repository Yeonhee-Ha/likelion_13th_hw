from django.contrib import admin
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name = "mainpage"),
    path('admin/', admin.site.urls),
    path('second', secondpage, name = "secondpage"),
    path('new-blog', new_blog, name="new-blog"),
    path('create', create, name="create"),
    path('<int:id>', detail, name = "detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]