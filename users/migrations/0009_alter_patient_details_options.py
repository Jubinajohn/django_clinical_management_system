# Generated by Django 4.1.1 on 2022-11-10 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_patient_details_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient_details',
            options={'verbose_name_plural': 'Patientdetails'},
        ),
    ]
