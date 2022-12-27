from django.db import models
from django.contrib.auth.models import AbstractUser
from .image_compress_snippet import compress_image

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    context = models.TextField()

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
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
    
class Opening(models.Model):
    class Meta:
        get_latest_by = "id"
        
    start_date = models.DateField()
    end_date = models.DateField()
    generation = models.SmallIntegerField()
    is_opened = models.BooleanField(default = False)
    title = models.CharField(max_length=100)
    question1 = models.TextField(max_length=1000, null=True, blank=True)
    question2 = models.TextField(max_length=1000, null=True, blank=True)
    question3 = models.TextField(max_length=1000, null=True, blank=True)
    question4 = models.TextField(max_length=1000, null=True, blank=True)
    question5 = models.TextField(max_length=1000, null=True, blank=True)
    question6 = models.TextField(max_length=1000, null=True, blank=True)
    question7 = models.TextField(max_length=1000, null=True, blank=True)
    question8 = models.TextField(max_length=1000, null=True, blank=True)
    question9 = models.TextField(max_length=1000, null=True, blank=True)
    question10 = models.TextField(max_length=1000, null=True, blank=True)

class About(models.Model):
    class Meta:
        get_latest_by = "id"

    body = models.TextField()
    image = models.ImageField(upload_to="Main")

    def save(self, *args, **kwargs):
        new_content_image = compress_image(self.image)
        self.image = new_content_image
        super().save(*args, **kwargs)

class Work(models.Model):
    duration = models.CharField(choices=(("1","1학기"),("1.5","여름방학"),("2","2학기")), max_length=10)
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="Work/%Y/%m/%d")

class Waiter(models.Model):
    name = models.CharField(max_length = 10)
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    choices = (
        ("지원", "지원"),
        ("심사", "심사"),
        ("활동", "활동"),
        ("기타", "기타")
    )
    question_type = models.CharField(choices=choices, max_length=10)
    question = models.TextField()
    answer = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)