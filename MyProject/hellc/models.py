from django.db import models
from myApp.models import CustomUser


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    level = models.SmallIntegerField(default = 1)
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email

class Calendar(models.Model):
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)
    log = models.TextField(default="{}")
    total_time = models.IntegerField(default = 0)
    is_recording = models.BooleanField(default = False)
    start_time = models.IntegerField(default = 0)
    status = models.CharField(max_length=100, default="start")
    
    def __str__(self):
        return self.user.email

class Room(models.Model):
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)
    host = models.IntegerField()
    
    guest_number = models.SmallIntegerField(default=0)
    guest1 = models.IntegerField(default=-1)
    guest2 = models.IntegerField(default=-1)
    guest3 = models.IntegerField(default=-1)
    guest4 = models.IntegerField(default=-1)
    
    def __str__(self):
        return self.user.email

class WorkLog(models.Model):
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    is_chest = models.BooleanField(default = False)
    is_back = models.BooleanField(default = False)
    is_shoulder = models.BooleanField(default = False)
    is_leg = models.BooleanField(default = False)
    is_arm = models.BooleanField(default = False)
    gym_name = models.CharField(max_length=100)
    year = models.SmallIntegerField(default = 0)
    month = models.SmallIntegerField(default = 0)
    date = models.SmallIntegerField(default = 0)