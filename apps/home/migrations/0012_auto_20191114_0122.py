# Generated by Django 2.2.6 on 2019-11-14 04:22

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_configuracoessite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracoessite',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BR'),
        ),
    ]
