from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    context = models.TextField()

class CustomUser(AbstractUser):
    # 더 추가 하고 싶은 유저 정보가 있다면 여기에 추가하시면 됩니다.
    def __str__(self):
        return self.email
