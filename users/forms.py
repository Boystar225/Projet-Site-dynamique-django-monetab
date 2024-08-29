from django import forms
from .models import User
# Create your models here.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('pseudos', 'password')