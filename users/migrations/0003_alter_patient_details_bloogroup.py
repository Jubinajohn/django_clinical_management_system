# Generated by Django 4.1.1 on 2022-10-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_contact_number_patient_details_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='bloogroup',
            field=models.CharField(blank=True, choices=[('type', '-------'), ('type', 'AB+'), ('type', 'AB-'), ('type', 'A+'), ('type', 'A-'), ('type', 'B+'), ('type', 'B-'), ('type', 'O+'), ('type', 'O-')], default=None, max_length=14),
        ),
    ]
