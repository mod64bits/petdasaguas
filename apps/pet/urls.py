from django.contrib import admin
from django.urls import path, include
from .views import PetDetalhe, ListPet


urlpatterns = [
    path('', ListPet.as_view(), name='pet-list'),
    path('pets/<slug:slug>/', PetDetalhe.as_view(), name='pet-detail'),
]
