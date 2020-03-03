from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Department, Position, Employee

def index(request):
    template = loader.get_template('employee/home/index.html')
    context = {
        'title': 'My Compant Home Page',
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('employee/home/dashboard.html')
    
    context = {
        'title': 'My Compant Department Page',
    }
    return HttpResponse(template.render(context, request))

def department_list(request):
    template = loader.get_template('employee/department/index.html')
    num_departments=Department.objects.count()
    departments=Department.objects.all()
    context = {
        'title': 'My Company Department Page',
        'departments': departments,
        'num_departments': num_departments
    }
    return HttpResponse(template.render(context, request))
    
def employee_list(request):
    template = loader.get_template('employee/employee/index.html')
    num_employees=Employee.objects.count()
    employees=Employee.objects.filter(updated_at__year=2020)
    # employees=Employee.objects.filter(updated_at__year=2020, department__name='Seo')
    # employees=Employee.objects.filter(updated_at__year=2020).filter(department__name='Seo')
    # employees=Employee.objects.filter(updated_at__year=2020).exclude(department__name='Seo')
    # employees=Employee.objects.order_by('updated_at')
    # employees=Employee.objects.order_by('-updated_at')
    context = {
        'title': 'My Company Employee Page',
        'employees': employees,
        'num_employees': num_employees
    }
    return HttpResponse(template.render(context, request))
