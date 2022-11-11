from email.policy import default
from django.db import models

# Create your models here.
class Doctor(models.Model):
    def __str__(self):
      return self.name
    doctor_id = models.IntegerField()
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=200,default='')
    qualification = models.CharField(max_length=250,default='')
    address = models.CharField(max_length=128,default='')


class Receptionist(models.Model):
  def __str__(self):
    return self.name
  reception_id = models.IntegerField()
  name = models.CharField(max_length=100)
  mobile_number = models.CharField(max_length=15)
  email = models.EmailField(max_length=200,default='')
  qualification = models.CharField(max_length=250,default='')
  address = models.CharField(max_length=128,default='')
  image = models.ImageField(blank = True,upload_to = 'images')

class Patient_history(models.Model):
  id_no = models.IntegerField()
  name = models.CharField(max_length=50)
  disease = models.CharField(max_length=100)
  medicine = models.CharField(max_length=100)
  date =  models.CharField(max_length=20)
  doctor = models.CharField(max_length=100)
  paid_amount = models.CharField(max_length=20)

class Recommended_med(models.Model):
  patient_id = models.IntegerField()
  name = models.CharField(max_length=50)
  symptoms = models.TextField(max_length=200)
  prescribed_drug = models.TextField(max_length=200)
  frequency = models.CharField(max_length=100)
  duration = models.CharField(max_length=100)
  quantity = models.CharField(max_length=100)
  signed_by = models.CharField(max_length=100)
  date = models.CharField(max_length=20,default='')
  time = models.CharField(max_length=20,default='')

GENDER_CHOICES  = (
    ("M", "M"),
    ("F", "F"),
) 
class Staffdetail(models.Model):
  def __str__(self):
      return self.name
  name = models.CharField(max_length=50)
  id_number = models.IntegerField()
  mobile = models.CharField(max_length=50)
  email = models.EmailField()
  gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
  position = models.CharField(max_length=100)
  employment_date = models.CharField(max_length=20)
  address = models.CharField(max_length=200)
  image = models.ImageField(blank = True,upload_to = 'images')