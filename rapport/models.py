from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()

    def _str_(self):
        return self.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)

    def _str_(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    def _str_(self):
        return self.user.username