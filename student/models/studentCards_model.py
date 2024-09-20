from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

class StudentCardsModel(DateTimeModel):
    student = models.ForeignKey('student.StudentModel', on_delete=models.CASCADE)
    reference = models.CharField(max_length=50)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
        verbose_name = "StudentCards"
        verbose_name_plural = "StudentCards"
