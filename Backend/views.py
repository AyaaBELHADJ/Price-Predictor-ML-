# views.py
from django.shortcuts import render, redirect
from .forms import FormulaireVoiture

def estimer_voiture(request):
    if request.method == 'POST':
        form = FormulaireVoiture(request.POST)
        if form.is_valid():
            voiture = form.save()
            # Logique pour estimer le prix de la voiture
            estimated_price = calculate_estimated_price(voiture)
            return render(request, 'mon_app/result.html', {'estimated_price': estimated_price})
    else:
        form = FormulaireVoiture()
    return render(request, 'mon_app/form.html', {'form': form})








































































































































































































































































































































































































































































































































































































































































































































