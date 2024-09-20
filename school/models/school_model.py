from django.db import models

from base.models.helpers.named_date_time_model import NamedDateTimeModel
from school.models.app_settings_model import AppSettingModel


class SchoolModel(NamedDateTimeModel):
    app = models.OneToOneField(AppSettingModel,related_name="school_app_id", on_delete=models.CASCADE)
    url_logo = models.URLField()
    
    

