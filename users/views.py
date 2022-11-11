from django.shortcuts import  render,redirect
from patient.models import Onlinebook
from users.models import Patient_details
from reception.models import Token
from users.forms import NewUserForm,LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
  if request.method == 'POST':
   form = NewUserForm(request.POST)
   if form.is_valid():
    form.save()
    return redirect('/cmsapp/home')
  form = NewUserForm(request.POST)
  context = {
    'form' : form,
  }
  return render(request,'users/register.html',context)

@login_required
def doctor(request):
   if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
    #  form.save()
     return redirect('/users/doc')
    
   form = NewUserForm(request.POST)
   return render(request, 'users/doctor.html',context={'form': form})  

def patientview(request):
  tokens = Token.objects.all()
  context = {
    'tokens':tokens
  }
  return render(request,'users/patient_view.html',context)

@login_required
def changepassword(request):
    return render(request,'users/changepassword.html')
  
def patient_detail(request,id):
 pats = Patient_details.objects.get(id=id)
 return render(request,'users/patientdetails.html',{'pats':pats})

def consultlist(request):
  book = Onlinebook.objects.all()
  context = {
    'book' : book
  }
  return render(request,'users/patconsultlist.html',context)

def viewconsultdet(request,id):
  book = Onlinebook.objects.get(id=id)
  context = {
        'book': book
  }
  return render(request,'users/view_conpatdetail.html',context)

def delete_token(request):
  tokens = Token.objects.all()
  if request.method == 'POST':
        tokens.delete()
    
        return redirect('/users/patview')

  return render(request,'users/delete_token.html',context={'tokens':tokens})

def delete_onlinelist(request):
   book = Onlinebook.objects.all()
   if request.method == 'POST':
        book.delete()
        return redirect('/users/conlist')
   return render(request,'users/delete_onlinepat.html')

