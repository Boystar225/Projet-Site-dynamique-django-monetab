from rest_framework import serializers
from school.models.app_settings_model import AppSettingModel

class AppsettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppSettingModel
        fields= '__all__'