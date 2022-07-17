import profile
from pyexpat import model
from tokenize import Triple
from turtle import title
from django.db import models

# Create your models here.
class Profile(models.Model):
    #id
    name = models.CharField(max_length=20, default="이름", null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=20, default="01000000000", null=True, blank=True)

class Url(models.Model):
    #id
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
