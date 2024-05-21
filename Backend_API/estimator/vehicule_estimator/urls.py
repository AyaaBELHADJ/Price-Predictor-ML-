
from django.urls import path
from .views import estimer_vehicule
from django.views.generic import TemplateView

urlpatterns = [

    path('estimation', estimer_vehicule, name='estimer_vehicule'),
    path('', TemplateView.as_view(template_name="index.html")),
    

]
