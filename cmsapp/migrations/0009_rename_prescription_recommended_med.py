# Generated by Django 4.1.1 on 2022-10-25 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0008_prescription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prescription',
            new_name='Recommended_med',
        ),
    ]
