from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.pet.models import CadastroPet
from .form import CadPet

class NovoPet(CreateView):
    model = CadastroPet
    form_class = CadPet
    template_name = 'core/novoPet.html'
