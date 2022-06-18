import string
from turtle import onclick
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField(max_length=None)
    Author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    Created_date=models.DateTimeField()
    Published_date=models.DateTimeField()
