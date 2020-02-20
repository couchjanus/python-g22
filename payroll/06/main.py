# main.py

import employees as r
from productivity import Productivity
from payroll import Payroll

def main():
    manager = r.Manager(1, 'Mary Poppins', 3000)
    secretary = r.Secretary(2, 'John Smith', 1500)
    sales_guy = r.SalesPerson(3, 'Kevin Bacon', 1000, 250)
    factory_worker = r.FactoryWorker(2, 'Jane Doe', 40, 15)

    employees = [
        manager,
        secretary,
        sales_guy,
        factory_worker,
    ]

    productivity = Productivity()
    productivity.track(employees, 40)

    payroll = Payroll()
    payroll.calculate_payroll(employees)
  
if __name__== "__main__":
    main()
