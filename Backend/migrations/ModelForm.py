from django import forms
from .models import Voiture

class FormulaireVoiture(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = [
            'price',
            'specs_annee',
            'specs_car_engine',
            'specs_couleur_auto',
            'specs_papiers',
            'specs_kilometrage',
            'specs_marque_voiture',
            'specs_modele',
            'specs_finition',
            'specs_energie',
            'specs_boite',
            'option0',
            'option1',
            'option2',
            'option3',
            'option4',
            'option5',
            'option6',
            'option7',
            'option8',
            'option9',
            'option10',
            'option11',
            'option12',
            'option13',
        ]

        widgets = {
            'option0': forms.CheckboxInput(),
            'option1': forms.CheckboxInput(),
            'option2': forms.CheckboxInput(),
            'option3': forms.CheckboxInput(),
            'option4': forms.CheckboxInput(),
            'option5': forms.CheckboxInput(),
            'option6': forms.CheckboxInput(),
            'option7': forms.CheckboxInput(),
            'option8': forms.CheckboxInput(),
            'option9': forms.CheckboxInput(),
            'option10': forms.CheckboxInput(),
            'option11': forms.CheckboxInput(),
            'option12': forms.CheckboxInput(),
            'option13': forms.CheckboxInput(),
        }