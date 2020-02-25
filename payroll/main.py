# main.py

import employees as r
from productivity import Productivity
from payroll import Payroll

import sqlite3

db_filename = 'employee.db'
        

def main():

    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        select id, name, emp_id, employees.salary, employees.commission, employees.rate, employees.hours from employee
        INNER JOIN employees ON employee.emp_id = employees.e_id;
        """)

        for row in cursor.fetchall():
            id, name, emp_id, salary, commission, rate, hours = row

            if (emp_id==1):
                manager = r.Manager(id, name, salary)
            elif (emp_id==2):
                secretary = r.Secretary(id, name, salary)
            elif (emp_id==3):
                sales_guy = r.SalesPerson(id, name, salary, commission)
            elif (emp_id==4):
                factory_worker = r.FactoryWorker(id, name, hours, rate)
    
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
