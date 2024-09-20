# rapport/forms.py
from django import forms

class RapportForm(forms.Form):
    CATEGORIES = [
        ('professeurs', 'Professeurs'),
        ('eleves', 'Élèves'),
        ('utilisateurs', 'Utilisateurs'),
    ]

    FORMATS = [
        ('pdf', 'PDF'),
        ('excel', 'Excel'),
    ]

    categorie = forms.ChoiceField(choices=CATEGORIES, label="Catégorie")
    format = forms.ChoiceField(choices=FORMATS, label="Format")