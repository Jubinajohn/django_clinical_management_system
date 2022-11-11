from random import choices
from django.db import models

# Create your models here.
DAY_CHOICES = (
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
)
TIME_CHOICES = (
   ("8.00PM to 8.45PM","8.00PM to 8.45PM"),
   ("9.00PM to 9.45PM","9.00PM to 9.45PM"),
)

class Onlinebook(models.Model):
  name = models.CharField(max_length=50)
  mobile_number = models.CharField(max_length=30)
  email = models.EmailField()
  select_day = models.CharField(max_length=20,choices=DAY_CHOICES)
  select_time = models.CharField(max_length=20,choices=TIME_CHOICES)
  location = models.CharField(max_length=50)

class Opticket(models.Model):
  date = models.CharField(max_length=20)
  token_no = models.IntegerField()
  op_no = models.IntegerField()
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=200)
  registration_fee = models.IntegerField()
  consultation_fee = models.IntegerField()
  total = models.IntegerField()
  cash = models.CharField(max_length=100)
  billed_by = models.CharField(max_length=100)
  time = models.CharField(max_length=20)
  doctor = models.CharField(max_length=50)
  
