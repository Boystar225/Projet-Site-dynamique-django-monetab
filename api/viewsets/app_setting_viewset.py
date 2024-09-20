from api.serializers.app_setting_serializer import AppsettingSerializer
from rest_framework import viewsets
from school.models.app_settings_model import AppSettingModel



class AppsettingViewSet(viewsets.ModelViewSet):
    serializer_class = AppsettingSerializer
    queryset = AppSettingModel.objects.all()