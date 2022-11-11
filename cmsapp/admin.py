from django.contrib import admin
from .models import Doctor, Receptionist,Staffdetail
# Register your models here.
# admin.site.register(Doctor)
# admin.site.register(Receptionist)
# admin.site.register(Staffdetail)

admin.site.site_header = 'LCC Administration'
admin.site.site_title = 'LCC'
admin.site.index_title = 'Life Care Clinic'

class DoctorAdmin(admin.ModelAdmin):
  list_display = ('id','doctor_id','name','mobile_number','email','qualification','address')
  search_fields = ('name',)
admin.site.register(Doctor,DoctorAdmin)

class ReceptionistAdmin(admin.ModelAdmin):
  list_display = ('id','image','reception_id','name','mobile_number','email','qualification','address')
  search_fields = ('name',)
admin.site.register(Receptionist,ReceptionistAdmin)

class StaffdetailAdmin(admin.ModelAdmin):
  list_display = ('id','image','name','id_number','mobile','email','gender','position','employment_date','address')
  search_fields = ('name',)
admin.site.register(Staffdetail,StaffdetailAdmin)
