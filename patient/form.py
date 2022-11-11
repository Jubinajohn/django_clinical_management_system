from tkinter.tix import Select
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

BLOODCHOICES = [
        ('type',  '-------'),
        ('type', 'AB+'),
        ('type', 'AB-'),
        ('type', 'A+'),
        ('type', 'A-'),
        ('type', 'B+'),
        ('type', 'B-'),
        ('type', 'O+'),
        ('type', 'O-'),
]
CHOICES = [
        ('type',  '-------'),
        ('F', 'Female',),
        ('M', 'Male',),
        ('Others', 'Others',),
]

class UserForm(UserCreationForm):
  name = forms.CharField(required=True ,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'Enter your name'}))
  age = forms.IntegerField(required=True ,widget=forms.TextInput(attrs={'class':'rounded-lg w-60 h-10'}))
  bloodgroup = forms.ChoiceField(required=True,choices=BLOODCHOICES,widget=forms.Select(attrs={'class':'rounded-lg w-60 h-10'}))
  gender = forms.ChoiceField(required=True,choices=CHOICES,widget=forms.Select(attrs={'class':'rounded-lg w-60 h-10'}))
  mobile_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'}))
  email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'📩Enter your email address'}))
  district = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'}))
  taluk = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'}))
  username = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'✉️Enter a username'}))
  password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'🔑Enter a password'}))
  password2 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'🗝️Confirm your password'}))
  address = forms.CharField(required=True,max_length=128,widget=forms.Textarea(attrs={'class':'rounded-lg w-96 h-24'}))


  class Meta:
    model = User
    fields = ('name','age','bloodgroup','gender','mobile_number','email','district','taluk','username','password1','password2','address')

def save(self,commit=True):
 user = super(UserForm,self).save(commit=False)
 user.email = self.cleaned_data['email']
 if commit:
    user.save()
    return user
  

class LoginForm(forms.Form):
  username = forms.CharField(required=True,widget=forms.TextInput())
  password = forms.CharField(required=True,widget=forms.TextInput())
  
  class Meta:
    model = User
    fields = ('username','password')

def save(self,commit=True):
  user = super(UserForm,self).save(commit=False)
  user.email = self.cleaned_data['email']
  if commit:
    user.save()
  return user
  