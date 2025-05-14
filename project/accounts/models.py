from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    nickname = models.TextField(max_length=10)
    major = models.TextField(null=True, max_length=30)
    hobby = models.TextField(null= True, max_length=20)
    birthday = models.DateField(null=True, blank=True)
    
    
class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name
