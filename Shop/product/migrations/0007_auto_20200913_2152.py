# Generated by Django 3.1.1 on 2020-09-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200913_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
