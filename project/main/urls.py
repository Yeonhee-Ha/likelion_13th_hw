from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"
urlpatterns = [
    path('', mainpage, name = "mainpage"),
    path('admin/', admin.site.urls),
    path('second', secondpage, name = "secondpage"),
    
    #blog
    path('new-blog', new_blog, name="new-blog"),
    path('create-blog', create_blog, name="create_blog"),
    path('detail/blog/<int:id>', detail_blog, name = "detail_blog"),
    path('edit/blog/<int:id>', edit_blog, name="edit_blog"),
    path('update/blog/<int:id>', update_blog, name="update_blog"),
    path('delete/blog/<int:id>', delete_blog, name="delete_blog"),
    
    #post
    path('new-post', new_post, name="new-post"),
    path('create-post', create_post, name="create_post"),
    path('detail/post/<int:id>', detail_post, name = "detail_post"),
    path('edit/post/<int:id>', edit_post, name="edit_post"),
    path('update/post/<int:id>', update_post, name="update_post"),
    path('delete/post/<int:id>', delete_post, name="delete_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)