# Generated by Django 3.1.13 on 2021-08-08 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_staff_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='address_line',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='city',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='province',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='suburb',
        ),
    ]