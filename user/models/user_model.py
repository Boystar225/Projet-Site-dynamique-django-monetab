from django.db import models
from django.contrib.auth.models import AbstractUser
# from base.models.helpers.date_time_model import DateTimeModel
from .roleUser_model import RoleUserModel

# Create your models here.
class CustomUserModel(AbstractUser):
    
    roleUser = models.ManyToManyField(RoleUserModel)
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE)
