# Generated by Django 3.2.18 on 2024-04-19 05:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0017_alter_productfeature_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='price',
            field=models.DecimalField(decimal_places=2, default=75, error_messages={'max_value': 'The price must be less than or equal to 100000.', 'min_value': 'The price must be greater than or equal to 0.'}, help_text='Price per month', max_digits=12, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)], verbose_name='Price'),
        ),
    ]