from django.contrib import admin

from user.models.user_model import CustomUserModel

# Register your models here.
admin.site.register(CustomUserModel)