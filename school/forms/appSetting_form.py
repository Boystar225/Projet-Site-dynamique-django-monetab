from django import forms
from school.models.app_settings_model import AppSettingModel


class AppSettingForms(forms.ModelForm):
    class Meta:
        model = AppSettingModel
        fields = "__all__"
        