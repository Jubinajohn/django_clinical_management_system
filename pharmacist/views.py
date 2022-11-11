from django.shortcuts import redirect, render
from requests import request
from pharmacist.models import MedicineInventory
from patient.form import UserForm
from pharmacist.forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
     form.save()
    return redirect('/cmsapp/home')
  form = RegisterForm(request.POST)
  context = {
    'form' : form,
  }
  return render(request,'pharmacist/phregister.html',context)

@login_required
def phhomepage(request):
  if request.method == 'POST':
        form2 = LoginForm(request.POST)
        if form2.is_valid():
          form2.save()
          return redirect('/pharmacist/phhome')
  form2 = UserForm(request.POST)
  return render(request,'pharmacist/phhomepage.html',context={'form2':form2})

def invent(request):
  inv = MedicineInventory.objects.all()
  return render(request,'pharmacist/inventory.html',context={'inv':inv})

@login_required
def add_inventory(request):
  if request.method == 'POST':
    serial_no = request.POST.get('serial_no')
    drug = request.POST.get('drug')
    purpose = request.POST.get('purpose')
    mfg_date = request.POST.get('mfg_date')
    exp_date = request.POST.get('exp_date')
    quantity = request.POST.get('quantity')
    unitprice = request.POST.get('unitprice')
    totalprice = request.POST.get('totalprice')
    inv = MedicineInventory(serial_no=serial_no,drug=drug,purpose=purpose,mfg_date=mfg_date,exp_date=exp_date,quantity=quantity,unitprice=unitprice,totalprice=totalprice)
    inv.save()
    return redirect('/pharmacist/invent')
  return render(request,'pharmacist/add_inventory.html')

def delete_inventory(request,id):
 inv = MedicineInventory.objects.get(id=id)
 if request.method == 'POST':
  inv.delete()
  return redirect('/pharmacist/invent')
 return render(request,'pharmacist/delete_inventory.html',context = {'inv':inv})

@login_required
def update_inventory(request,id):
  inv = MedicineInventory.objects.get(id=id)
  if request.method == 'POST':
      inv.serial_no= request.POST.get('serial_no')
      inv.drug= request.POST.get('drug')
      inv.purpose= request.POST.get('purpose')
      inv.mfg_date = request.POST.get('mfg_date')
      inv.exp_date = request.POST.get('exp_date')
      inv.quantity = request.POST.get('quantity')
      inv.unitprice = request.POST.get('unitprice')
      inv.totalprice = request.POST.get('totalprice')
      inv.save()
      return redirect('/pharmacist/invent')
  context = {
        'inv':inv
    }
  return render(request,'pharmacist/update_inventory.html',context)
  