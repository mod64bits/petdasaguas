# Generated by Django 2.2.6 on 2019-12-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_veterianriosprceiros_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterianriosprceiros',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Link  Facebook '),
        ),
        migrations.AlterField(
            model_name='veterianriosprceiros',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Link instagram  '),
        ),
        migrations.AlterField(
            model_name='veterianriosprceiros',
            name='site',
            field=models.URLField(blank=True, null=True, verbose_name='Link site  '),
        ),
        migrations.AlterField(
            model_name='veterianriosprceiros',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Link Twitter  '),
        ),
    ]