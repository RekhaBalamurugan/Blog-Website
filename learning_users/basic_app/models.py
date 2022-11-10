from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(default="Logo_1.png", upload_to='profile_pics',blank=True)

    def __str__(self):
        return f'{self.user.username} UserProfileInfo'

class Loginuser(models.Model):
    #username = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Post(models.Model):
    title= models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    slug=models.CharField(max_length=100,null=True)
    time= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("blogpost", kwargs={"slug": self.slug})

