from django import forms
from user.models.user_model import CustomUserModel


class UserFoms(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = "__all__"
        