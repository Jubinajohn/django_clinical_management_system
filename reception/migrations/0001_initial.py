# Generated by Django 4.1.1 on 2022-10-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_number', models.IntegerField()),
                ('doctor', models.CharField(choices=[('Dr.George T John', 'Dr.George T John')], max_length=50)),
                ('patient_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('bloodgroup', models.CharField(choices=[('AB+', 'AB+'), ('AB-', 'AB-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], max_length=14)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('taluk', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
