# Generated by Django 3.2.12 on 2022-11-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20221111_1809'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packages',
            new_name='Package',
        ),
    ]