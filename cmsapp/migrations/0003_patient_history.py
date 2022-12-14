# Generated by Django 4.1.1 on 2022-10-09 00:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_receptionist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('disease', models.CharField(max_length=100)),
                ('medicine', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('doctor', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.patient_history')),
            ],
        ),
    ]
