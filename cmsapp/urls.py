from django.urls import path
from .views import  add_patienthist, add_patmedicine, hist_list, homeview, index,list,homeview,patienthistory,about_us,contact_us

app_name = 'cmsapp'

urlpatterns = [
   path('hello/',index),
   path('doct/',list),
   path('home/',homeview,name='homeview'),
   path('pathist/<int:id>/',patienthistory,name='patienthist'),
   path('histlist/',hist_list,name='histlist'),
   path('aboutus/',about_us,name='aboutus'),
   path('contact/',contact_us,name='contactus'),
   #add
   path('addpatmed/',add_patmedicine,name='addpatmedicine'),
   path('addpathist/',add_patienthist,name='addpatienthist'),
]
