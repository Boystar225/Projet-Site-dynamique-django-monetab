from django import forms
from user.models.roleUser_model import RoleUserModel


class RoleUserFoms(forms.ModelForm):
    class Meta:
        model = RoleUserModel
        fields = "__all__"
        