# Generated by Django 2.2.6 on 2019-11-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191113_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiros',
            name='height_field',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='parceiros',
            name='width_field',
            field=models.IntegerField(default=200),
        ),
    ]