from django.contrib import admin
from .models import applicant, contacts
# Register your models here.

class applicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'student_Id', 'security', 'amount')
    list_filter = ('amount', 'security')
    search_fields = ('name', 'security')

admin.site.register(applicant, applicantAdmin)

class contactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'message')
    
admin.site.register(contacts, contactsAdmin)   