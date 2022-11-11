from multiprocessing import context
from django.shortcuts import  redirect, render
from reception.forms import  RegisterForm,LoginForm
from users.models import Patient_details
from reception.models import Addmedicine, Token,Bill
from cmsapp.models import Recommended_med
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
  return render(request,'reception/recregister.html',context)

@login_required
def rechomepage(request):
   if request.method == 'POST':
        form1 = LoginForm(request.POST)
        if form1.is_valid():
         form1.save()
        return redirect('/reception/rec')
   form1 = RegisterForm(request.POST)
   return render(request,'reception/rechome.html',context={'form1':form1})

@login_required
def addpatient(request):
  if request.method=='POST':
    patient_id = request.POST.get('patient_id')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    bloodgroup = request.POST.get('bloodgroup')
    age = request.POST.get('age')
    address = request.POST.get('address')
    taluk = request.POST.get('taluk')
    mobile_number = request.POST.get('mobile_number')
    email = request.POST.get('email')
    pat = Patient_details(patient_id=patient_id,name=name,gender=gender,bloodgroup=bloodgroup,age=age,address=address,taluk=taluk,mobile_number=mobile_number,email=email)
    pat.save()
    return redirect('/reception/viewpat')
  return render(request,'reception/add_patient.html')

@login_required
def changepassword(request):
  return render(request,'reception/password.html')

@login_required  
def createtoken(request):
  if request.method=='POST':
    token_number = request.POST.get('token_number')
    date = request.POST.get('date')
    doctor = request.POST.get('doctor')
    patient_id = request.POST.get('patient_id')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    bloodgroup = request.POST.get('bloodgroup')
    age = request.POST.get('age')
    address = request.POST.get('address')
    taluk = request.POST.get('taluk')
    mobile_number = request.POST.get('mobile_number')
    email = request.POST.get('email')
    tok = Token(token_number=token_number,date=date,doctor=doctor,patient_id=patient_id,name=name,gender=gender,bloodgroup=bloodgroup,age=age,address=address,taluk=taluk,mobile_number=mobile_number,email=email)
    tok.save()
    return redirect('/users/patview')
  return render(request,'reception/create_token.html')

def viewpatmedicine(request,id):
  med = Recommended_med.objects.get(id=id)
  context = {
    'med' : med
  }
  return render(request,'reception/view_patmedicine.html',context)

def viewpatient(request):
  pats = Patient_details.objects.all()
  context = {
    'pats':pats
  }
  return render(request,'reception/view_patient.html',context)

def token(request,id):
  tokens = Token.objects.get(id=id)
  context = {
        'tokens': tokens
  }
  return render(request,'reception/token.html',context)

def patmedicine(request):
  med = Recommended_med.objects.all()
  context = {
    'med' : med
  }
  return render(request,'reception/patmedicine.html',context)

@login_required
def add_bill(request):
  if request.method=='POST':
    bill_no = request.POST.get('bill_no')
    op_no = request.POST.get('op_no')
    name = request.POST.get('name')
    address = request.POST.get('address')
    
    prescribed_by = request.POST.get('prescribed_by')
    doctor_type = request.POST.get('doctor_type')
   
    net_amount = request.POST.get('net_amount')
    cash = request.POST.get('cash')
    billed_by = request.POST.get('billed_by')
    date = request.POST.get('date')
    time = request.POST.get('time')
    bill = Bill(bill_no=bill_no,op_no=op_no,name=name,address=address,prescribed_by=prescribed_by,doctor_type=doctor_type,net_amount=net_amount,cash=cash,billed_by=billed_by,date=date,time=time)
    bill.save()
    return redirect('/reception/billdet')
  return render(request,'reception/add_bill.html')

def bill_detail(request):
  bill = Bill.objects.all()
  medi = Addmedicine.objects.all()
  
  return render(request,'reception/bill_detail.html',{'bill': bill, 'medi':medi})

def delete_bill(request):
  bill = Bill.objects.all()
  if request.method == 'POST':
        bill.delete()
    
        return redirect('/reception/billdet')

  return render(request,'reception/delete_bill.html', {'bill':bill})
  
def delete_med(request):
 medi = Addmedicine.objects.all()
    
 if request.method == 'POST':   
        medi.delete()
        return redirect('/reception/billdet')

 return render(request,'reception/delete_med.html', {'medi':medi})
 
@login_required      
def add_medicine(request):
  if request.method=='POST':
    serial_no = request.POST.get('serial_no')
    name_of_drugs = request.POST.get('name_of_drugs')
    batch = request.POST.get('batch')
    expiry = request.POST.get('expiry')
    quantity = request.POST.get('quantity')
    rate = request.POST.get('rate')
    amount = request.POST.get('amount')
    medi = Addmedicine(serial_no=serial_no,name_of_drugs=name_of_drugs,batch=batch,expiry=expiry,quantity=quantity,rate=rate,amount=amount)
    medi.save()
    return redirect('/reception/billdet')
  return render(request,'reception/add_medicine.html')

def delete_presmedicine(request):
   med = Recommended_med.objects.all()
   if request.method == 'POST':
        med.delete()
        return redirect('/reception/patmed')
   return render(request,'reception/delete_presmedicine.html')

