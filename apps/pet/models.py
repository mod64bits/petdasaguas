from django.db import models
from apps.core.signals import create_slug
from django.urls import reverse
from django.db.models import signals
from sorl.thumbnail import ImageField


class CategoriaPet(models.Model):
    nome = models.CharField('Nome', help_text='Nome da Categoria', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria Pet'
        verbose_name_plural = 'Categorias Pets'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cstegoria_pet', kwargs={'slug': self.slug})


signals.post_save.connect(create_slug, sender=CategoriaPet)


class Especie(models.Model):
    nome = models.CharField('Nome', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Especie)


class CadastroPet(models.Model):
    especie = models.ForeignKey(Especie, name='Especie', on_delete=models.CASCADE)
    nome = models.CharField('Nome', help_text='Exemplo TóTó', max_length=50)
    categoria = models.ForeignKey(CategoriaPet, name='Categoria', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    descricao = models.TextField('Descrição')
    fotoPerfil = ImageField(upload_to='adocao')

    atotado = models.BooleanField('Adotado?', default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Cadastro Pet'
        verbose_name_plural = 'Cadastros Pets'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'slug': self.slug})


signals.post_save.connect(create_slug, sender=CadastroPet)


class PetImagens(models.Model):
    pet = models.ForeignKey(CadastroPet, on_delete=models.CASCADE, related_name='petCadastrado')
    imagem = ImageField(upload_to='adocao')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'pet'

    # def __str__(self):
    #     return self.pet


signals.post_save.connect(create_slug, sender=PetImagens)



