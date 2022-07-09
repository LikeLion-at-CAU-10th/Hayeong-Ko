from django.db import models

# Create your models here.
class Profile(models.Model):
    #id
    name = models.CharField(max_length=20, default="이름", null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=20, default="01000000000", null=True, blank=True)