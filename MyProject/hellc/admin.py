from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pet)
admin.site.register(Calendar)
admin.site.register(Room)
admin.site.register(WorkLog)