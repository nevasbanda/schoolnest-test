from django import forms
from . models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_logo', 'school_name', 'country', 'province', 'district', 'suburb', 'school_lat', 'school_lng', 'school_motto', 'school_about', 'school_address', 'school_contact', 'school_email', 'school_website', 'school_vacancy', 'school_academics']
        widgets = {
            'school_logo': forms.FileInput(attrs={'class': 'form-control'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'suburb': forms.TextInput(attrs={'class': 'form-control'}),
            'school_lat': forms.TextInput(attrs={'class': 'form-control'}),
            'school_lng': forms.TextInput(attrs={'class': 'form-control'}),
            'school_motto': forms.TextInput(attrs={'class': 'form-control'}),
            'school_about': forms.TextInput(attrs={'class': 'form-control'}),
            'school_address': forms.TextInput(attrs={'class': 'form-control'}),
            'school_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'school_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'school_website': forms.TextInput(attrs={'class': 'form-control'}),
            'school_vacancy': forms.TextInput(attrs={'class': 'form-control'}),
            'school_academics': forms.TextInput(attrs={'class': 'form-control'}),
        }






