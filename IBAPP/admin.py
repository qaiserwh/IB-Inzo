from .models import  *
from django.contrib import admin

# Register your models here.

    
class IbAccountPage1Admin(admin.ModelAdmin):
    search_fields=['name','IB_number']
    list_display=['name','IB_number','client_NO','typye']

   
admin.site.register(IbAccountPage1,IbAccountPage1Admin)
admin.site.register(IbAccountPage2,IbAccountPage1Admin)
admin.site.register(IbAccountPage3,IbAccountPage1Admin)
admin.site.register(IbAccountPage4,IbAccountPage1Admin)
admin.site.register(IbAccountPage5,IbAccountPage1Admin)
admin.site.register(Course)
admin.site.register(About)
admin.site.register(Opinion)
admin.site.register(Offer)

