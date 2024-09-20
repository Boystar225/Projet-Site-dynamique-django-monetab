from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.
class AbsenceModel(DateTimeModel):
    student = models.ForeignKey('student.StudentModel', on_delete=models.CASCADE, related_name="student_ids")
    absence_date = models.DateField()
    absence_number = models.IntegerField()

    class Meta:
        verbose_name = "Absence"
        verbose_name_plural = "Absences"
