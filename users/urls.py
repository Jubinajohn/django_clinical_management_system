from django import views
from django.urls import path
from .views import changepassword, consultlist, doctor,register,patientview,patient_detail, viewconsultdet,delete_token,delete_onlinelist
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns = [
  path('register/',register,name='register'),
  path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
  path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
  path('doc/',doctor,name='doctor'),
  path('patview/',patientview,name='patientview'),
  path('pass/',changepassword,name='changepass'),
  path('patdet/<int:id>/',patient_detail,name='patient_detail'),
  path('conlist/',consultlist,name='consultlist'),
  path('conpatdet/<int:id>/',viewconsultdet,name='consultpat'),
  #delete
  path('deltok/',delete_token,name='deletetoken'),
  path('delonline/',delete_onlinelist,name='deleteonline'),
]
