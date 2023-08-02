from django import forms
from .models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text', 'profile_photo']


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text', 'profile_photo']

