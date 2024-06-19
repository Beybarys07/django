from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=150)
    description = models.TextField

    def __str__(self):
        return self.user.first_name
    

class Mobels(models.Model):
    mebel=models.CharField(max_length=255)
    content=models.CharField(max_length=1500)
    CodeTMC=models.CharField(max_length=500,null=True)
    Height=models.IntegerField(null=True)
    Width=models.IntegerField(null=True)
    Length=models.IntegerField(null=True)
    Weight=models.IntegerField(null=True)
    is_published=models.BooleanField(blank=True)
    photo=models.ImageField('photo=photos/%Y/%n?%d/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.mebel
    
    def get_absolute_url(self):
        return reverse('postdetail', kwargs={'Mobels_id': self.pk})
    

class Category(models.Model):
    Name=models.CharField(max_length=150)
    CodeTMC=models.CharField(max_length=500,null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

 
    def __str__(self):
        return self.Name 


class Luxury(models.Model):
    Name1=models.CharField(max_length=100)
    Text1=models.CharField(max_length=100)
    CodeTMC=models.CharField(max_length=500,null=True)
    Height1=models.IntegerField(null=True)
    Width1=models.IntegerField(null=True)
    Length1=models.IntegerField(null=True)
    Weight1=models.IntegerField(null=True)
    category=models.ForeignKey('Category', on_delete=models.PROTECT, null=True)



