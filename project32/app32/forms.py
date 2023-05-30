from django import forms
from .models import applicant, contacts

class Application(forms.ModelForm):
    class Meta:
        model = applicant
        fields = '__all__'

class Contact(forms.ModelForm):
    class Meta:
        model = contacts
        fields = '__all__'