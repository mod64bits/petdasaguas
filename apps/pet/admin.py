from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import CategoriaPet, CadastroPet, PetImagens, Especie


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    list_display_links = ['nome']
    list_filter = ['nome', 'slug']
    search_fields = ['nome', 'slug']


class PetImageInline(AdminImageMixin, admin.TabularInline):
    model = PetImagens
    # extra = 5


class MyModelAdmin(admin.ModelAdmin):
    inlines = [PetImageInline]


class CadastroPetAdmin(admin.ModelAdmin):
    list_display =['nome', 'descricao', 'atotado']
    list_display_links = ['nome']
    list_filter = ['nome']
    search_fields = ['nome', 'categoria']
    list_editable = ['atotado']
    inlines = [PetImageInline]
    # def get_img(self, obj):
    #     if obj.imagem1:
    #         return u'<img width="50px" height="50px" src="/media/adocao/%s" />' % obj.imagem1
    #     else:
    #         return u'Sem Imagem'
    # get_img.short_description = 'Imagem'
    # get_img.allow_tags = True



admin.site.register(CategoriaPet, CategoriaAdmin)
admin.site.register(CadastroPet, CadastroPetAdmin)
admin.site.register(Especie)


