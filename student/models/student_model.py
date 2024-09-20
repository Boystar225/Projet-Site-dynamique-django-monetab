from django.db import models
from base.models.helpers.person_model import PersonModel



class StudentModel(PersonModel):

    matricule = models.CharField(max_length=20)
    phone_number_father = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.matricule}"