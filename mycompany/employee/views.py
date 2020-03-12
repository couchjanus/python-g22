# employee/views.py 
from django.shortcuts import render

from .models import Department, Position, Employee
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
def my_view(request):
    pass

from django.contrib.auth.mixins import LoginRequiredMixin

# mixin для представлений на основе классов.
from django.contrib.auth.mixins import PermissionRequiredMixin


# class DashboardView(LoginRequiredMixin, TemplateView):
#     template_name = "employee/dashboard.html"

class DashboardView(TemplateView):
    template_name = "employee/dashboard.html"

class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'employee/department/department_list.html'

class DepartmentCreate(CreateView):
    model = Department
    fields = '__all__'
    template_name = 'employee/department/department_form.html'

    def get_success_url(self):
        return reverse('departments')

class DepartmentUpdate(UpdateView):
    model = Department
    fields = '__all__'
    template_name = 'employee/department/department_form.html'

    def get_success_url(self):
        return reverse('departments')


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'employee/department/department_detail.html'


class PositionListView(ListView):
    model = Position
    context_object_name = 'positions'
    template_name = 'employee/position/position_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My Company Position Page'
        return context

class PositionDetailView(DetailView):
    model = Position
    template_name = 'employee/position/position_detail.html'

class PositionCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'employee.can_create_position'
    # Or multiple permissions
    # permission_required = ('employee.can_edit_position', 'employee.can_create_position')
    model = Position
    fields = '__all__'
    template_name = 'employee/position/position_form.html'

    def get_success_url(self):
        return reverse('positions')

class PositionUpdate(UpdateView):
    model = Position
    fields = '__all__'
    template_name = 'employee/position/position_form.html'

    def get_success_url(self):
        return reverse('positions')

class PositionDelete(DeleteView):
    model = Position
    template_name = 'employee/position/position_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('positions')

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee/employee/employee_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee/employee/employee_form.html'

    def get_success_url(self):
        return reverse('employees')

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee/employee_detail.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employee/employee/employee_form.html'

    def get_success_url(self):
        return reverse('employees')
