# Generated by Django 2.2.6 on 2019-12-09 13:02

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20191209_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterianriosprceiros',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='BR'),
        ),
    ]