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

class Paper(models.Model):
    applicant_name = models.CharField(max_length=5)
    applicant_email = models.EmailField()
    applicant_major = models.CharField(max_length = 50)
    context = models.TextField()
    reg_time = models.DateTimeField(auto_now_add=True)
    mod_time = models.DateTimeField(auto_now=True)
    year = models.IntegerField()

    def __str__(self):
        return "지원자: " + self.applicant_name + " / 이메일 :" + self.applicant_email


class PaperAdmin(models.Model):
    year = models.IntegerField()
    is_opened = models.BooleanField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class ActLog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 500)
    image = models.ImageField(upload_to="ActLog")

class Notice(models.Model):
    title = models.CharField(max_length = 50)
    context = models.TextField()
    reg_time = models.DateTimeField(auto_now_add = True)
    mod_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()




