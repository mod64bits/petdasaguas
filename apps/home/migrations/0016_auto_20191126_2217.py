# Generated by Django 2.2.6 on 2019-11-27 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_configuracoessite_sobre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parceiros',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='parceiros',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='imagem',
            field=models.ImageField(help_text='Selecione uma Foto', upload_to='adocao', verbose_name='Foto'),
        ),
    ]