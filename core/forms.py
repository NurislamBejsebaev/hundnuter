from django import forms
from .models import Vacancy, Company


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary',
                  'description', 'email']


class VacancyEditform(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'salary',
                  'description', 'email']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'num_employees', 'is_hunting']
        exclude = ['created_at']


class CompanyEdit(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'num_employees', 'is_hunting']
        exclude = ['created_at']

