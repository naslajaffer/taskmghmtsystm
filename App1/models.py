from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Taskdata(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Taskname=models.CharField(max_length=40)
    Startdate=models.DateField()
    Duedate=models.DateField()
    Description=models.CharField(max_length=40)
    Status=models.CharField(max_length=20)
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=50)
    Phone=models.IntegerField()
    DOB=models.DateField()
    Profilepicture=models.ImageField()
