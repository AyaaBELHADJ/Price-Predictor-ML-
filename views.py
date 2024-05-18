from django.shortcuts import render
from django.http import JsonResponse
from .models import Car

def process_car_form(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire depuis la requête POST
        specs_annee = request.POST.get('specs_annee')
        specs_car_engine = request.POST.get('specs_car_engine')
        specs_couleur_auto = request.POST.get('specs_couleur_auto')
        # Récupérez les autres champs de formulaire de la même manière

        # Créer un nouvel objet Car et enregistrer dans la base de données
        car = Car.objects.create(
            specs_annee=specs_annee,
            specs_car_engine=specs_car_engine,
            specs_couleur_auto=specs_couleur_auto,
            # Enregistrez les autres champs dans votre modèle Car
        )

        # Retourner une réponse JSON indiquant que le formulaire a été traité avec succès
        return JsonResponse({'message': 'Formulaire traité avec succès!'})

    # Si la méthode de requête n'est pas POST, retourner une erreur
    return JsonResponse({'error': 'Méthode de requête non valide'})











































