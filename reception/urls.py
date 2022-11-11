from django.urls import path
from django.contrib.auth import views as authentication_views
from reception.views import changepassword,delete_bill,rechomepage,createtoken,addpatient,viewpatient,token,viewpatmedicine,patmedicine,add_bill,bill_detail,add_medicine,delete_med,register,delete_presmedicine

app_name = 'reception'

urlpatterns = [
  path('register/',register,name='register'),
  path('rec/',rechomepage,name='rechome'),
  path('chpass/',changepassword,name='password'),
  path('token/',createtoken,name='token'),
  path('viewpatmed/<int:id>/',viewpatmedicine,name='viewpatmed'),
  path('viewpat/',viewpatient,name='viewpatient'),
  path('login/',authentication_views.LoginView.as_view(template_name='reception/login2.html'),name='login1'),
  path('tokdet/<int:id>/',token,name='tokendetails'),
  path('patmed/',patmedicine,name='patmedicine'),
  path('billdet/',bill_detail,name='billdetail'),
  #add
  path('addpat/',addpatient,name='addpatient'),
  path('addbill/',add_bill,name='addbill'),
  path('addmed/',add_medicine,name='addmedicine'),
  #delete
  path('billdelete/',delete_bill,name='billdelete'),
  path('meddel/',delete_med,name='meddelete'),
  path('delpresmed/',delete_presmedicine,name='deletepresmedicine'),
]
