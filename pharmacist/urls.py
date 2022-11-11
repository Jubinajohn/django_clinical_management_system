from django.urls import path
from .views import phhomepage, register,add_inventory,delete_inventory,update_inventory,invent
from django.contrib.auth import views as authentication_views

app_name = 'pharmacist'

urlpatterns = [
  path('phreg/',register,name='register'),
  path('login/',authentication_views.LoginView.as_view(template_name='pharmacist/login3.html'),name='login3'),
  path('phhome/',phhomepage,name='phhomepage'),
  path('invent',invent,name='invent'),
  #add
  path('addinvent/',add_inventory,name='addinventory'),
  #delete
  path('delinvent/<int:id>/',delete_inventory,name='delinventory'),
  #update
  path('updateinvent/<int:id>/',update_inventory,name='updateinventory'),
]