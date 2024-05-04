from django.db import models

class Car(models.Model):
    specs_annee = models.IntegerField()
    specs_car_engine = models.CharField(max_length=100)
    specs_couleur_auto = models.CharField(max_length=100)
    specs_papiers = models.CharField(max_length=100)
    specs_kilometrage = models.IntegerField()
    specs_marque_voiture = models.CharField(max_length=100)
    specs_modele = models.CharField(max_length=100)
    specs_finition = models.CharField(max_length=100)
    specs_energie = models.CharField(max_length=100)
    specs_boite = models.CharField(max_length=100)
    option0 = models.BooleanField(default=False)  # Champs pour l'option 0
    option1 = models.BooleanField(default=False)  # Champs pour l'option 1
    option2 = models.BooleanField(default=False)  # Champs pour l'option 2
    option3 = models.BooleanField(default=False)  # Champs pour l'option 3
    option4 = models.BooleanField(default=False)  # Champs pour l'option 4
    option5 = models.BooleanField(default=False)  # Champs pour l'option 5
    option6 = models.BooleanField(default=False)  # Champs pour l'option 6
    option7 = models.BooleanField(default=False)  # Champs pour l'option 7
    option8 = models.BooleanField(default=False)  # Champs pour l'option 8
    option9 = models.BooleanField(default=False)  # Champs pour l'option 9
    option10 = models.BooleanField(default=False) # Champs pour l'option 10
    option11 = models.BooleanField(default=False) # Champs pour l'option 11
    option12 = models.BooleanField(default=False) # Champs pour l'option 12
    option13 = models.BooleanField(default=False) # Champs pour l'option 13


























