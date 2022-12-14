# Generated by Django 4.1.1 on 2022-10-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_bloogroup_patient_details_bloodgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_details',
            name='address',
            field=models.TextField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='bloodgroup',
            field=models.CharField(choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], default=0, max_length=14),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='mobile_number',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
