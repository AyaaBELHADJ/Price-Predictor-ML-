
from django.shortcuts import render
from django.http import JsonResponse
import json



def estimer_vehicule(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        # Effectuez le traitement nécessaire avec les données reçues
        marque  = data.get('marque')
        modele = data.get('modele')
        annee = data.get('annee')
        energie = data.get('energie')
        kilometrage = data.get('kilometrage')
        boite = data.get('boite')
        couleur = data.get('couleur')
        finitio = data.get('finition')
        moteur = data.get('moteur')
        papiers = data.get('papiers')
        options = data.get('options', [])
        
        # Simuler une estimation (remplacez par votre logique d'estimation réelle)
        estimation = 5000000  # Exemple d'estimation

        return JsonResponse({'estimation': estimation})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
