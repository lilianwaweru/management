from django import forms
from .models import Master,Education,Work

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['first_name','other_names','identification_number','nssf_number','nhif_number','date_of_birth','employee_number','employee_position','image']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['secondary_shool','higher_education','level_of_education','course','other_certificates']


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['company','position','duration','tasks']
