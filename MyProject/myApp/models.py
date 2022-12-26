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

class Application(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11,default="01012345678")
    email = models.EmailField(unique=True)
    password = models.IntegerField(default=1234)
    major = models.CharField(max_length=100, blank = True, null = True)
    student_id = models.IntegerField(unique=True, null=True)
    create_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    generation = models.IntegerField(default = 0)
    answer1 = models.TextField(null=True, blank=True)
    answer2 = models.TextField(null=True, blank=True)
    answer3 = models.TextField(null=True, blank=True)
    answer4 = models.TextField(null=True, blank=True)
    answer5 = models.TextField(null=True, blank=True)
    answer6 = models.TextField(null=True, blank=True)
    answer7 = models.TextField(null=True, blank=True)
    answer8 = models.TextField(null=True, blank=True)
    answer9 = models.TextField(null=True, blank=True)
    answer10 = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    



