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
            'Climatisation',
            'toit_ouvrant ',
            ' ABS',
            ' ESP',
            'Radare_de_recule',
            ' Direction',
            ' assiste  ',
            'Retroviseurs  ',
            'Phares_antibrouillard ',
            ' Radio_cd',
            ' Alarme',
            ' Phare_xenon  ',
            'Jantes_Alliage',
            ' Feux_du_jour',
             'Vitres_electistique'
        ]

        widgets = {
            'Climatisation': forms.CheckboxInput(),
            'toit_ouvrant ': forms.CheckboxInput(),
            ' ABS': forms.CheckboxInput(),
            ' ESP': forms.CheckboxInput(),
            'Radare_de_recule': forms.CheckboxInput(),
            ' Direction': forms.CheckboxInput(),
            ' assiste  ': forms.CheckboxInput(),
            'Retroviseurs ': forms.CheckboxInput(),
            'Phares_antibrouillard': forms.CheckboxInput(),
            ' Radio_cd': forms.CheckboxInput(),
            ' Alarme': forms.CheckboxInput(),
            'Phare_xenon':forms.CheckboxInput(),
            'Jantes_Alliage': forms.CheckboxInput(),
            ' Feux_du_jour': forms.CheckboxInput(),
            'Vitres_electistique': forms.CheckboxInput(),
        }