from django.db import models

# Create your models here.
class LikeLion(models.Model):
    CHOICES = (
        ('기획', "기획"),
        ('백엔드', "백엔드"),
        ("프론트엔드", "프론트엔드")
    )

    name = models.CharField(max_length=20, default="", unique=True)
    part = models.CharField(max_length=20, choices=CHOICES, default="백엔드")
    age = models.IntegerField(default=20)
    bio = models.TextField(default="소개를 입력해주세요", null=True)
    profile_image = models.ImageField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
