from django import forms
from base.models.helpers.person_model import PersonModel
from teacher.models.teacher_model import TeacherModel

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
        model = TeacherModel
        fields = "__all__"
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'gender' :forms.RadioSelect(choices=PersonModel.GENDER_CHOICES), 
        }