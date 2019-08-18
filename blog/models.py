from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blog_technology(models.Model):
    tittle=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to="images/")
    def summary(self):
        return self.body[:200]
    def __str__(self):
        return self.tittle

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
      return self.user.username
