# Generated by Django 2.2.6 on 2019-12-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20191209_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='veterianriosprceiros',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link instagram  '),
        ),
        migrations.AddField(
            model_name='veterianriosprceiros',
            name='site',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Link site  '),
        ),
    ]