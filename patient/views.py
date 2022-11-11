from django.shortcuts import redirect, render
from patient.models import Onlinebook, Opticket
from patient.form import  UserForm,LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def patregister(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
     form.save()
    return redirect('/cmsapp/home')
  form = UserForm(request.POST)
  context = {
    'form' : form,
  }
  return render(request,'patient/patregister.html',context)

@login_required
def pathome(request):
   if request.method == 'POST':
        form3 = LoginForm(request.POST)
        if form3.is_valid():
          form3.save()
          return redirect('/patient/pathome')
   form3 = UserForm(request.POST)
   return render(request,'patient/pathome.html',context={'form3':form3})

@login_required
def onlinebook(request):
  if request.method=='POST':
    name = request.POST.get('name')
    mobile_number = request.POST.get('mobile_number')
    email = request.POST.get('email')
    select_day = request.POST.get('select_day')
    select_time = request.POST.get('select_time')
    location = request.POST.get('location')
    book = Onlinebook(name=name,mobile_number=mobile_number,email=email,select_day=select_day,select_time=select_time,location=location)
    book.save()
    return redirect('/users/conlist')
  return render(request,'patient/onlinebook.html')

@login_required 
def op_ticket(request):
  if request.method=='POST':
    token_no = request.POST.get('token_no')
    op_no = request.POST.get('op_no')
    name = request.POST.get('name')
    address = request.POST.get('address')
    registration_fee = request.POST.get('registration_fee')
    consultation_fee = request.POST.get('consultation_fee')
    total = request.POST.get('total')
    cash = request.POST.get('cash')
    billed_by = request.POST.get('billed_by')
    doctor = request.POST.get('doctor')
    time = request.POST.get('time')
    date = request.POST.get('date')
    op = Opticket(token_no=token_no,op_no=op_no,name=name,address=address,registration_fee=registration_fee,consultation_fee=consultation_fee,total=total,cash=cash,billed_by=billed_by,doctor=doctor,date=date,time=time)
    op.save()
    return redirect('/patient/optick')
  return render(request,'patient/op_ticketform.html')

def opticket(request):
  op = Opticket.objects.all()
  return render(request,'patient/op_ticket.html',context={'op':op})

def delete_ticket(request,id):
  op = Opticket.objects.get(id=id)
  if request.method == 'POST':
    op.delete()
    return redirect('/patient/optick')
  return render(request,'patient/delete_ticket.html',context={'op':op})
