from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


# Create your models here.
class AppSettingModel(DateTimeModel):
    smtp_server = models.CharField(max_length=50) 
    smtp_port = models.IntegerField()
    smtp_username = models.CharField(max_length=50)
    smtp_password = models.CharField(max_length=50)

    class Meta:
        verbose_name = "AppSetting"
        verbose_name_plural = "AppSettings"

    def __str__(self):
        return f"{self.smtp_server}, {self.smtp_username}"
