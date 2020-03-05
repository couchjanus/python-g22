"""mycompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('payroll/', views.home, name="home"),
    path('departments/', views.department_list, name="departments"),
    path('department/', views.create_department, name="department"),
    path('position/', views.position_list, name='position_index'),
    path('create_position/', views.PositionCreate.as_view(), name='position_create'),
    path('employees/', views.employee_list, name="employees"),
    path('create_employee/', views.create_employee, name="create_employee"),
]
