from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Prefetch
from django.db import connection
from django.views import View
from django.views.generic import DetailView, ListView
from .models import CadastroPet, PetImagens


class PetDetalhe(DetailView):
    model = CadastroPet

    template_name = 'home/PetDetalhe.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # fotos = PetImagens.objects.select_related('pet').prefetch_related('pet__petCadastrado')
        # aux = [photo.petCadastrado.filter(spicy=True) for photo in fotos]
        # for pet in fotos:
        #     aux = pet.petCadastrado.all()
        # for foto in fotos:
        #     aux = fotos.imagem.all

        # pet = CadastroPet.objects.get(id=1)
        # p = PetImagens.objects.get(pet)
        s = self.object.slug
        petSlug = PetImagens.objects.filter(pet__slug=s)
        # fotos = PetImagens.objects.filter(pet__id=petSlug)




        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['petList'] = petSlug
        # context['petList'] = PetImagens.objects.filter(id__in=has_)
        return context


class ListPet(ListView):
    model = CadastroPet
    template_name = 'home/ListaPet.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['pet'] = CadastroPet.objects.all()
        return context

