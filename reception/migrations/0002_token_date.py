# Generated by Django 4.1.1 on 2022-10-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='date',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]
