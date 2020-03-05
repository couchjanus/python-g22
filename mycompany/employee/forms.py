from django import forms
from .models import Department, Position

from django.core.exceptions import ValidationError
import datetime 


class DepartmentForm(forms.Form):
    name = forms.CharField(label='Department name', max_length=250)


GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=25,
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name','name':'first_name'}), error_messages={'required': 'Enter First Name'})
    
    middle_name = forms.CharField(
        max_length=25,
        label="Midels Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Midels Name','name':'middle_name'}), error_messages={'required': 'Enter Midels Name'})

    last_name = forms.CharField(
        max_length=25,
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name','name':'last_name'}), error_messages={'required': 'Enter Last Name'})
    
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email','name':'email'}),
        error_messages={'required': 'Enter email address'})
       
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    position = forms.ModelChoiceField(queryset=Position.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=GENDER_CHOICES)
    
    birth_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
        }))

    def clean_birth_date(self):
        data = self.cleaned_data['birth_date']
        
        # Проверка того, что дата не выходит за "нижнюю" границу.
        if data > datetime.date.today() - datetime.timedelta(days = 365*18):
            raise ValidationError('Invalid date - too young')
        # Проверка того, то дата не выходит за "верхнюю" границу.
        if data < datetime.date.today() - datetime.timedelta(days = 365*60):
            raise ValidationError('Invalid date - too old')
    	# всегда надо возвращать очищенные данные.
        return data

    monthly_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), max_digits=14, decimal_places=4)
        
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)
    
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Employee bio','name':'bio'}), required=False, label="Employee bio")
