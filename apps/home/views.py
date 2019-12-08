from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Parceiros, Slider, VeterianrioLogo, ConfiguracoesSite


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parceiros'] = Parceiros.objects.all()
        context['Slide'] = Slider.objects.all()
        context['logos'] = VeterianrioLogo.objects.all()
        context['configuracoesSite'] = ConfiguracoesSite.objects.all()
        return context



