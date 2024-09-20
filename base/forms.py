from django import forms
from .models.helpers.adress_model import AdressModel

class AdressFoms(forms.ModelForm):
    class Meta:
        model = AdressModel
        fields = "__all__"
        