from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import ActLog, Blog, CustomUser, Notice, Paper, PaperAdmin
# Register your models here.

admin.site.register(Blog)
admin.site.register(Paper)
admin.site.register(PaperAdmin)
admin.site.register(ActLog)
admin.site.register(Notice)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']

admin.site.register(CustomUser, CustomUserAdmin)