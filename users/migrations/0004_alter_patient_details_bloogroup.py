# Generated by Django 4.1.1 on 2022-10-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_patient_details_bloogroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='bloogroup',
            field=models.CharField(choices=[('type', '-------'), ('type', 'AB+'), ('type', 'AB-'), ('type', 'A+'), ('type', 'A-'), ('type', 'B+'), ('type', 'B-'), ('type', 'O+'), ('type', 'O-')], max_length=14),
        ),
    ]
