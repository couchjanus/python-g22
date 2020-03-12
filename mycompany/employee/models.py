from django.db import models
from django.urls import reverse 
# Create your models here.

class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models.

    All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AbstractBaseModel):
    """Department represents the sector a set of employees belongs to."""

    name = models.CharField(verbose_name = "Department name", max_length=250, unique=True, help_text="Enter department name")

    class Meta:
        ordering = ["name", "-updated_at"]
        permissions = (("can_create_department", "Can create department"),("can_edit_department", "Can edit department"),("can_delete_department", "Can delete department"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular department instance."""
        return reverse('department-detail', args=[str(self.id)])

class Position(AbstractBaseModel):
    """Position represents the sector a set of employees belongs to."""

    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ["name", "-updated_at"]
        permissions = (("can_create_position", "Can create position"),("can_edit_position", "Can edit position"),("can_delete_position", "Can delete position"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular position instance."""
        return reverse('position-detail', args=[str(self.id)])

class Employee(AbstractBaseModel):
    """Employee represents the people from a given department."""

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    first_name = models.CharField(max_length=25, help_text="Enter first name")
    middle_name = models.CharField(max_length=25, help_text="Enter midels name")
    last_name = models.CharField(max_length=25, help_text="Enter last name")
    email = models.EmailField(unique=True, help_text="Enter email")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    birth_date = models.DateField(null=False, blank=False)
    monthly_salary = models.DecimalField(max_digits=14, decimal_places=4, null=False, blank=False)
    active = models.BooleanField(default=True)
    bio = models.TextField(null = True, blank = True, help_text="Enter employee bio")

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Employees"
        ordering = ["first_name", "-updated_at"]
        permissions = (("can_create_employee", "Can create employee"),("can_edit_employee", "Can edit employee"),("can_delete_employee", "Can delete employee"),)

    def age(self):
        from datetime import date
        return date.today().year - self.birth_date.year - ((date.today().month, date.today().day) < (self.birth_date.month, self.birth_date.day)) if self.birth_date else None

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])
    
    def __str__(self):
        return ' ' .join([self.first_name, self.middle_name, self.last_name])

    @property
    def name(self):
        """
        Возвращаем полное имя
        """
        return "%s %s" % (self.first_name, self.last_name)
