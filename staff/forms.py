from django import forms
from .models import Master,Work

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['first_name','other_names','department','employee_number']





class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['identification_number','nssf_number','nhif_number','date_of_birth','employee_position','company','position','duration','tasks','secondary_shool','higher_education','level_of_education','course','other_certificates','employee','image']
