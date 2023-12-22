from django.db import models
from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


  

class ItUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null= True)
    address = models.TextField(blank=True, null= True)
    profile_pic = models.FileField(upload_to='images/profiles/',null= True)
    position = models.CharField(max_length=30,null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
