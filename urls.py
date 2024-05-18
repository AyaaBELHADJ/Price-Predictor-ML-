from django.contrib import admin
from django.urls import path
from . import views  # Assurez-vous que ce module existe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estimer/', views.estimer, name='estimer'),  # Exemple de route vers une vue appelée "estimer"
]























































































































































