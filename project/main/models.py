from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null = False, blank=False, on_delete=models.CASCADE) 
    content = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:20]
    

class Post(models.Model):
    title = models.CharField(max_length=100) 
    writer = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.CharField(max_length=50, default="일반") 
    content = models.TextField()              
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='post/', blank=True, null=True)  # 이미지 업로드

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=False, blank=False, on_delete=models.CASCADE)
    
    def str (self):
        return self.blog.title + " : " + self.content[:20] + "by" + self.writer.profile.nickname
    
    
