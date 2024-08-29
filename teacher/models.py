from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birth_date = models.DateField()
    
    disponibility = models.BooleanField()
    courses = models.CharField(max_length=15)
    number = models.CharField(max_length=10)
    country  = models.CharField(max_length=20)
    lesson = models.CharField(max_length=100)
    next_meet = models.CharField(max_length=100)