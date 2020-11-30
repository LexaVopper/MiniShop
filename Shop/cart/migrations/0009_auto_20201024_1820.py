# Generated by Django 3.1.1 on 2020-10-24 15:20

import cart.models
from django.db import migrations
import django_enum_choices.choice_builders
import django_enum_choices.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20200910_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stage',
            field=django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('На складе', 'На складе'), ('В пути', 'В пути'), ('Доставлено', 'Доставлено')], default=None, enum_class=cart.models.StageGeneration, max_length=10),
        ),
    ]
