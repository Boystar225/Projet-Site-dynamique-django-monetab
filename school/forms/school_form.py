from django import forms
from school.models.school_model import SchoolModel


class SchoolForms(forms.ModelForm):
    class Meta:
        model = SchoolModel
        fields = "__all__"
        