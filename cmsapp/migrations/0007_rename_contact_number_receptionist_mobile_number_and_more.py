# Generated by Django 4.1.1 on 2022-10-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_alter_doctor_address_alter_doctor_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receptionist',
            old_name='contact_number',
            new_name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='state',
        ),
        migrations.AddField(
            model_name='receptionist',
            name='address',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='receptionist',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='receptionist',
            name='qualification',
            field=models.CharField(default='', max_length=250),
        ),
    ]
