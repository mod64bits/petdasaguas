from django.contrib import admin
from .models import Parceiros, Slider, VeterianrioLogo, ConfiguracoesSite


class ParceirosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'imagem', 'created', 'modified')
    list_filter = ['nome', 'imagem']

    def queryset(self, request):
        qs = super(ParceirosAdmin, self).queryset(request)
        return qs.order_by("nome")


class SliderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem', 'created', 'modified')
    list_filter = ['titulo', 'created']


class VeterianrioLogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'created', 'modified')
    list_filter = ['nome', 'created']


class ConfiguracoesSiteAdmin(admin.ModelAdmin):
    list_display = ('tituloSite', 'telefone', 'created', 'modified')
    list_filter = ['tituloSite', 'created']



admin.site.register(Parceiros, ParceirosAdmin)
admin.site.register(ConfiguracoesSite, ConfiguracoesSiteAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(VeterianrioLogo, VeterianrioLogoAdmin)
