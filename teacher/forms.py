from django import forms

from .models import Teacher

# # Create your forms here.
# class Teacher(forms.Form):
#     name = forms.CharField()
#     last_name = forms.CharField()
#     birth_date = forms.DateField()
#     gender = forms.CharField()
#     matricule = forms.CharField()
#     courses = forms.CharField()
#     number = forms.CharField()
#     ville = forms.CharField()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name","last_name","birth_date","disponibility","courses","number","country","lesson","next_meet"]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'disponibility': forms.CheckboxInput(),
            'number':forms.NumberInput(attrs={'type': 'number'}),
            
        }