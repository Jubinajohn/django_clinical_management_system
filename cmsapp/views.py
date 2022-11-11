# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from cmsapp.models import Doctor, Patient_history,Recommended_med
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
  return HttpResponse("hello world!")

def list(request):
  doct = Doctor()
  doct.doctor_id = 1002
  doct.name = 'M L Mathew'
  doct.mobile_number = 9544632139
  doct.email = 'mathew233@gmail.com'
  doct.qualification = 'MBBS'
  doct.address = 'Madathil House Vaduthala PO Ernakulam'
  doct.save()
  return HttpResponse('<h1>Hello Doctor!</h1>')

def homeview(request):
    return render(request, 'cmsapp/home.html')

def patienthistory(request,id):
  hist = Patient_history.objects.get(id=id)
  context = {
        'hist':hist
  }
  return render(request,'cmsapp/patient_history.html',context)

@login_required 
def add_patmedicine(request):
  if request.method=='POST':
    patient_id = request.POST.get('patient_id')
    name = request.POST.get('name')
    symptoms = request.POST.get('symptoms')
    prescribed_drug = request.POST.get('prescribed_drug')
    frequency = request.POST.get('frequency')
    duration = request.POST.get('duration')
    quantity = request.POST.get('quantity')
    signed_by = request.POST.get('signed_by')
    date = request.POST.get('date')
    time = request.POST.get('time')
    prescribe = Recommended_med(patient_id=patient_id,name=name,symptoms=symptoms,prescribed_drug=prescribed_drug,frequency=frequency,duration=duration,quantity=quantity,signed_by=signed_by,date=date,time=time)
    prescribe.save()
    return redirect('/reception/patmed')
  return render(request,'cmsapp/add_patmedicine.html')

@login_required  
def add_patienthist(request):
   if request.method=='POST':
    id_no = request.POST.get('id_no')
    name = request.POST.get('name')
    disease = request.POST.get('disease')
    medicine = request.POST.get('medicine')
    doctor = request.POST.get('doctor')
    date = request.POST.get('date')
    paid_amount = request.POST.get('paid_amount')
    hist = Patient_history(id_no=id_no,name=name,disease=disease,medicine=medicine,doctor=doctor,date=date,paid_amount=paid_amount)
    hist.save()
    return redirect('/cmsapp/histlist')
   return render(request,'cmsapp/add_patienthist.html')
  
def hist_list(request):
  hist = Patient_history.objects.all()
  context = {
    'hist' : hist
  }
  return render(request,'cmsapp/histlist.html',context)

def about_us(request):
  return render(request,'cmsapp/about_us.html')

def contact_us(request):
  return render(request,'cmsapp/contact.html')
  