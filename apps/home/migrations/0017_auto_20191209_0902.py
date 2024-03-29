# Generated by Django 2.2.6 on 2019-12-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191126_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeterianriosPrceiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Clinica', max_length=50, verbose_name='Nome')),
                ('imagem', models.ImageField(help_text='Selecione uma Foto de Boa Qualidade', upload_to='veterianioParceiro', verbose_name='Imagem')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link  Facebook ')),
                ('twitter', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link Twitter  ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Veterianrio Parceiro',
                'verbose_name_plural': 'Veterianrios Parceiros',
                'ordering': ['nome'],
            },
        ),
        migrations.DeleteModel(
            name='VeterianrioLogo',
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='imagem',
            field=models.ImageField(help_text='Selecione uma Foto', upload_to='parceiros', verbose_name='Foto'),
        ),
    ]
