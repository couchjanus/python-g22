# main.py

from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee
from commission_employee import CommissionEmployee
from payroll import Payroll
import disgruntled

salary_employee = SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')

payroll = Payroll()

payroll.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_employee
])
