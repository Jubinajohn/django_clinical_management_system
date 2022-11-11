# Generated by Django 4.1.1 on 2022-10-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_alter_token_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=50)),
                ('op_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=128)),
                ('serial_no', models.IntegerField()),
                ('name_of_drugs', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=100)),
                ('expiry', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('prescribed_by', models.CharField(max_length=50)),
                ('doctor_type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=20)),
                ('net_amount', models.CharField(max_length=20)),
                ('cash', models.CharField(max_length=100)),
                ('billed_by', models.CharField(max_length=50)),
                ('date', models.CharField(default='', max_length=20)),
                ('time', models.CharField(default='', max_length=20)),
            ],
        ),
    ]