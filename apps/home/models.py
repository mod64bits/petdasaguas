from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Parceiros(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do Parceiro')
    descricao = models.TextField('Descrição Parceiro')
    telefone = PhoneNumberField(region="BR", null=True, blank=True)
    site = models.URLField('Site', null=True, blank=True)
    imagem = models.ImageField('Foto', upload_to='parceiros', help_text='Selecione uma Foto')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Slider(models.Model):
    titulo = models.CharField('Titulo', max_length=50, help_text='Titulo do Slider')
    descricao = models.TextField('Descrição Parceiro')
    imagem = models.ImageField('Imagem', upload_to='slide', help_text='Selecione uma Foto de Boa Qualidade')
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class VeterianriosPrceiros(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome da Clinica')
    imagem = models.ImageField('Imagem', upload_to='veterianioParceiro', help_text='Selecione uma Foto de Boa Qualidade')
    telefone = PhoneNumberField(region="BR", blank=True, null=True)
    facebook = models.URLField('Link  Facebook ',  max_length=200, null=True, blank=True)
    twitter = models.URLField('Link Twitter  ', max_length=200, null=True, blank=True)
    site = models.URLField('Link site  ', max_length=200, null=True, blank=True)
    instagram = models.URLField('Link instagram  ', max_length=200, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Veterianrio Parceiro'
        verbose_name_plural = 'Veterianrios Parceiros'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class ConfiguracoesSite(models.Model):
    tituloSite = models.CharField('Titulo do Site', max_length=50, help_text="Titulo da Aba")
    telefone = PhoneNumberField(region="BR", blank=True, null=True)
    email = models.EmailField('Email', blank=True)
    endereco = models.CharField('Endereço', max_length=150, blank=True)
    sobre = models.TextField('Uma Breve Descrição', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'
        ordering = ['tituloSite']

    def __str__(self):
        return self.tituloSite





