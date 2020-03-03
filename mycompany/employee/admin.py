from django.contrib import admin

# Register your models here.
from .models import Department, Position, Employee

admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)