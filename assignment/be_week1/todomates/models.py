from django.db import models

# Create your models here.
class Category(models.Model):
    #id 
    title = models.CharField(max_length=50, default="제목", null=True, blank=True)
    view_auth = models.IntegerField(default=0, null=True, blank=True)
    color = models.CharField(max_length=10, default="#000000", null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)