from django.db import models
from myApp.models import CustomUser


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    level = models.SmallIntegerField(default = 1)
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)

class Calendar(models.Model):
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)
    log = models.TextField()
    total_time = models.IntegerField(default = 0)
    is_recording = models.BooleanField(default = False)
    start_time = models.IntegerField(default = 0)

class Room(models.Model):
    user = models.ForeignKey("myApp.CustomUser", verbose_name=("user"), on_delete=models.CASCADE)
    host = models.ForeignKey("hellc.Pet", verbose_name=("pet"), on_delete=models.CASCADE)
    
    guest_number = models.SmallIntegerField()
    guest1 = models.ForeignKey("hellc.Pet", verbose_name=("pet"), on_delete=models.CASCADE)
    guest2 = models.ForeignKey("hellc.Pet", verbose_name=("pet"), on_delete=models.CASCADE)
    guest3 = models.ForeignKey("hellc.Pet", verbose_name=("pet"), on_delete=models.CASCADE)
    guest4 = models.ForeignKey("hellc.Pet", verbose_name=("pet"), on_delete=models.CASCADE)
