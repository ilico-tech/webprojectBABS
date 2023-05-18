
from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.LocationVoiture,name='voiture'),
    path('autoexpress/<int:id>/', views.DetailVoiture, name='detail'),
    path('louermavoiture/',views.LouermaVoiture,name='louer'),
    path('Modifiervoiture/<int:id>/',views.ModifierVoiture,name='modifier'),
    path('Supprimervoiture/<int:id>/', views.SupprimerVoiture, name='supprimer'),



]