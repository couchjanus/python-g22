from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),

    path('departments/',  views.DepartmentListView.as_view(), name="departments"),
    path('department_create/', views.DepartmentCreate.as_view(), name='department_create'),

    path('department/<int:pk>',
         views.DepartmentDetailView.as_view(), name='department-detail'),
    path('department/<int:pk>/update/', views.DepartmentUpdate.as_view(), name='department-update'),

    path('positions/', views.PositionListView.as_view(), name='positions'),
    path('position_create/', views.PositionCreate.as_view(), name='position_create'),

    path('position/<int:pk>', views.PositionDetailView.as_view(), name='position-detail'),

    path('position/<int:pk>/update/', views.PositionUpdate.as_view(), name='position-update'),

    path('position/<int:pk>/delete/', views.PositionDelete.as_view(), name='position-delete'),

    path('employees/',  views.EmployeeListView.as_view(), name="employees"),
    path('employee_create/', views.EmployeeCreate.as_view(), name='employee_create'),

    path('employee/<int:pk>',
         views.EmployeeDetailView.as_view(), name='employee-detail'),
    
]
