from django.urls import path
from .views import onlinebook, patregister,pathome,op_ticket,opticket,delete_ticket
from django.contrib.auth import views as authentication_views

app_name = 'patient'

urlpatterns = [
  path('patreg/',patregister,name='patregister'),
  path('login/',authentication_views.LoginView.as_view(template_name='patient/login1.html'),name='login2'),
  path('pathome/',pathome,name='pathome'),
  path('book/',onlinebook,name='onlinebook'),
  path('opticket/',op_ticket,name='opticket'),
  path('optick/',opticket,name='optick'),
  #delete
  path('delticket/<int:id>/',delete_ticket,name='delete_ticket'),
]
