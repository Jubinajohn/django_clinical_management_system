from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

BLOOD_CHOICES = (
  
       
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),

)

DOCTOR_CHOICES = (
  ('Dr.George T John', 'Dr.George T John'),
)

class Token(models.Model):
  token_number = models.IntegerField()
  date = models.CharField(max_length=20,default='')
  doctor = models.CharField(max_length=50,choices=DOCTOR_CHOICES)
  patient_id = models.IntegerField()
  name = models.CharField(max_length=50)
  gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
  bloodgroup = models.CharField(max_length=14,choices=BLOOD_CHOICES)
  age = models.IntegerField()
  address = models.CharField(max_length=128)
  taluk = models.CharField(max_length=30)
  mobile_number = models.CharField(max_length=100)
  email = models.EmailField()


class Bill(models.Model):
  bill_no = models.CharField(max_length=50)
  op_no = models.IntegerField()
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=128)
  prescribed_by = models.CharField(max_length=50)
  doctor_type = models.CharField(max_length=100)
  net_amount = models.CharField(max_length=20)
  cash = models.CharField(max_length=100)
  billed_by = models.CharField(max_length=50)
  date = models.CharField(max_length=20,default='')
  time = models.CharField(max_length=20,default='')

class Addmedicine(models.Model):
  serial_no = models.CharField(max_length=20)
  name_of_drugs = models.CharField(max_length=200)
  batch = models.CharField(max_length=100)
  expiry = models.CharField(max_length=20)
  quantity = models.CharField(max_length=50)
  rate = models.CharField(max_length=50)
  amount = models.CharField(max_length=20)
