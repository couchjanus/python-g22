from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Department, Position, Employee
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import DepartmentForm, EmployeeForm

from django.urls import reverse

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

def position_list(request):
    template = loader.get_template('employee/position/index.html')
    num_positions=Position.objects.count()
    positions=Position.objects.all()
    context = {
        'title': 'My Company Position Page',
        'positions': positions,
        'num_positions': num_positions
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


def create_department(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DepartmentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            dep = Department()
            dep.name=request.POST.get('name')
            dep.save()
            form.cleaned_data['name']
            # redirect to a new URL:
            return HttpResponseRedirect('/departments/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DepartmentForm()

    return render(request, 'employee/department/department_form.html', {'form': form})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data as required

            employee = Employee()
            employee.first_name=request.POST.get('first_name')
            employee.middle_name=request.POST.get('middle_name')
            employee.last_name=request.POST.get('last_name')
            employee.email=request.POST.get('email')
            employee.bio=request.POST.get('bio')
            employee.birth_date = form.cleaned_data['birth_date']

            # employee.birth_date=request.POST.get('birth_date')
            employee.monthly_salary=request.POST.get('monthly_salary')
            employee.gender=request.POST.get('gender')
            
            employee.department = Department.objects.get(id=request.POST.get('department'))

            employee.position = Position.objects.get(id=request.POST.get('position'))

            employee.active=True if request.POST.get('active') == 'on' else False

            form.cleaned_data['first_name']
            form.cleaned_data['middle_name']
            form.cleaned_data['last_name']
            form.cleaned_data['email']
            form.cleaned_data['department']
            form.cleaned_data['position']
            form.cleaned_data['gender']
            form.cleaned_data['birth_date']
            form.cleaned_data['monthly_salary']
            form.cleaned_data['active']
            form.cleaned_data['bio']

            employee.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/employees/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmployeeForm()

    return render(request, 'employee/employee/employee_form.html', {'form': form})

class PositionCreate(CreateView):
    model = Position
    fields = '__all__'
    template_name = 'employee/position/position_form.html'

    def get_success_url(self):
        return reverse('position_index')
