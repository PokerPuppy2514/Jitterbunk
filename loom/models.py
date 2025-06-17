import datetime

from django.db import models
from django.utils import timezone

class LoomVideo(models.Model):
    title = models.CharField(max_length=200)
    link =  models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transcript = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    team = models.CharField(max_length=200) #maybe put as foreign key
    tags = models.CharField(max_length=200) #max 10 tags maybe put as a collection 
    created_at = models.DateTimeField('created at')




class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    team = models.CharField(max_length=200)



