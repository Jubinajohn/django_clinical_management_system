from asyncio.windows_events import NULL
from email.policy import default
from random import choices
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


class Patient_details(models.Model):
  def __str__(self):
    return self.name
  # id = models.IntegerField(primary_key=True)
  patient_id = models.IntegerField()
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=200)
  mobile_number = models.CharField(max_length=15,default=0)
  age = models.IntegerField() 
  bloodgroup = models.CharField(max_length=14,choices=BLOOD_CHOICES,default=0)
  gender = models.CharField(max_length=20, choices=GENDER_CHOICES,default='')
  taluk = models.CharField(max_length=50,default='')
  address = models.TextField(max_length=128,default='')
 
  
  class Meta:
        verbose_name_plural = "Patientdetails"