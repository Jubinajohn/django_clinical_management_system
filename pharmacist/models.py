from django.db import models

# Create your models here.

class MedicineInventory(models.Model):
  serial_no = models.IntegerField()
  drug = models.CharField(max_length=200)
  purpose = models.CharField(max_length=500)
  mfg_date = models.CharField(max_length=50)
  exp_date = models.CharField(max_length=50)
  quantity = models.CharField(max_length=50)
  unitprice = models.CharField(max_length=50)
  totalprice = models.IntegerField()

