# Generated by Django 4.1.1 on 2022-10-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0010_rename_patient_id_patient_history_id_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_history',
            name='paid_amount',
            field=models.CharField(max_length=20),
        ),
    ]
