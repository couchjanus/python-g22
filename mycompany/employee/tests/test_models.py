from django.test import TestCase

from employee.models import Employee, Department, Position
# Create your tests here.

class EmployeeTestClass(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     print("setUpTestData: Run once to set up non-modified data for all class methods.")
    #     pass

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Position.objects.create(name='manager')
        Department.objects.create(name='CEO')
        Employee.objects.create(first_name='Big', middle_name='Dic', last_name='Bob', birth_date='1999-02-02', monthly_salary='1234', department_id='1', position_id='1')

    def test_first_name_label(self):
        # Получение объекта для тестирования
        employee=Employee.objects.get(id=1)
        # Получение метаданных поля для получения необходимых значений
        field_label = employee._meta.get_field('first_name').verbose_name
        # Сравнить значение с ожидаемым результатом
        self.assertEquals(field_label,'first name')

    def test_birth_date_label(self):
        # Получение объекта для тестирования
        employee=Employee.objects.get(id=1)
        
        field_label = employee._meta.get_field('birth_date').verbose_name
        self.assertEquals(field_label,'birth')

    def test_first_name_max_length(self):
        # Получение объекта для тестирования
        employee=Employee.objects.get(id=1)
        max_length = employee._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        # Получение объекта для тестирования
        employee=Employee.objects.get(id=1)
        expected_object_name = '%s %s %s' % (employee.first_name, employee.middle_name, employee.last_name)
        self.assertEquals(expected_object_name,str(employee))

    def test_get_absolute_url(self):
        # Получение объекта для тестирования
        employee=Employee.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(employee.get_absolute_url(),'/employee/employee/1')
