from django.contrib import admin
from users.models  import Patient_details 

# Register your models here.
# admin.site.register(Patient_details)
class Patient_detailsAdmin(admin.ModelAdmin):
  list_display = ('id','patient_id','name','email','mobile_number','age','bloodgroup','gender','taluk','address')
  search_fields = ('name',)
admin.site.register(Patient_details,Patient_detailsAdmin)

