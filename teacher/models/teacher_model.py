from django.db import models
from base.models.helpers.person_model import PersonModel



class TeacherModel(PersonModel):

    available = models.BooleanField(default=False)
    speciality = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"