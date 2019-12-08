
from django.contrib import admin
from django.urls import path, include
from .views import NovoPet


urlpatterns = [
    path('petadd', NovoPet.as_view(), name='novo-pat'),
]
