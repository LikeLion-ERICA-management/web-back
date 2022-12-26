from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import ActLog, Blog, CustomUser, Notice, Paper, PaperAdmin, Application, Opening, About, Work
# Register your models here.

admin.site.register(Blog)
admin.site.register(Paper)
admin.site.register(PaperAdmin)
admin.site.register(ActLog)
admin.site.register(Notice)
admin.site.register(Application)
admin.site.register(Opening)
admin.site.register(About)
admin.site.register(Work)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'is_admin',
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)