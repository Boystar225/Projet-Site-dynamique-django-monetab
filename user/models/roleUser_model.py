from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class RoleUserModel(DateTimeModel):

    role = models.CharField(max_length=50)

    class Meta:
        verbose_name = "RoleUser"
        verbose_name_plural = "RoleUsers"

    def __str__(self):
        return f"{self.role}"