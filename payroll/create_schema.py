# create_schema.py
import os
import sqlite3

db_filename = 'employee.db'
schema_filename = 'schema.sql'

# Выполняем поиск файла базы данных перед его открытием с помощью connect()
db_is_new = not os.path.exists(db_filename)

# Скрипт создает пустой файл, если файл не существует.
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Schema Created Successfully')
        
        print('Inserting initial data')

        conn.executescript("""
        insert into employees (salary, commission, rate, hours) values (3000, null, null, null);
        insert into employees (salary, commission, rate, hours) values (1500, null, null, null);
        insert into employees (salary, commission, rate, hours) values (1000, 250, null, null);
        insert into employees (salary, commission, rate, hours) values (null, null, 13, 40);

        insert into employee (name, emp_id)  values ('Mary Poppins', 1);
        insert into employee (name, emp_id)  values ('John Smith', 2);
        insert into employee (name, emp_id)  values ('Kevin Bacon', 3);
        insert into employee (name, emp_id)  values ('Jane Doe', 4);
   
        """)

    else:
        print('Database exists, assume schema does, too.')
