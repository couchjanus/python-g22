# main.py

import employees.roles as roles
import productivity
import payroll

manager = roles.Manager(1, 'Mary Poppins', 3000)
secretary = roles.Secretary(2, 'John Smith', 1500)
sales_guy = roles.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = roles.FactoryWorker(2, 'Jane Doe', 40, 15)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]

productivity = productivity.Productivity()
productivity.track(employees, 40)

payroll = payroll.Payroll()
payroll.calculate_payroll(employees)
