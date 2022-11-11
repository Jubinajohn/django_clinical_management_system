from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'}))
  qualification = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'})) 
  mobile = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10'}))
  email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'📩Enter your email address'}))
  username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'Enter a username with your personal id number'}))
  password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'🔑Enter the password'}))
  password2 = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'rounded-lg w-96 h-10','placeholder':'🔑Confirm password'}))
  address = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'rounded-lg w-96 h-24'}))
  
  class Meta:
    model = User
    fields = ('name','qualification','mobile','email','username','password1','password2','address')
  
def save(self,commit=True):
 user = super(RegisterForm,self).save(commit=False)
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
  user = super(RegisterForm,self).save(commit=False)
  user.email = self.cleaned_data['email']
  if commit:
    user.save()
  return user
  