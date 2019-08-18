from django.db import models

# Create your models here.
class job(models.Model):
    tittle=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/")
    summary=models.CharField(max_length=600)
