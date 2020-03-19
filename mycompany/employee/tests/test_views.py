from django.test import TestCase

# Create your tests here.

from employee.models import Employee, Department, Position
from django.urls import reverse

class EmployeeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Position.objects.create(name='manager')
        Department.objects.create(name='CEO')
        #Create 13 employees for tests
        number_of_employees = 13
        for employee_num in range(number_of_employees):
            Employee.objects.create(first_name='Chris %s' % employee_num, middle_name='Cat %s' % employee_num, last_name = 'Surname %s' % employee_num, birth_date='1999-02-02', monthly_salary='1234', department_id='1', position_id='1', email='cat%s@example.com' % employee_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/employee/employees/')
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employees'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employees'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'employee/employee/employee_list.html')
   
