-- Schema for application.

-- Projects are high-level activities made up of tasks
create table employees (
    e_id        integer primary key autoincrement not null,
    salary      integer,
    commission  integer,
    rate        integer,
    hours       integer
);

-- Tasks are steps that can be taken to complete a employees
create table employee (
    id        integer primary key autoincrement not null,
    name      text,
    emp_id   integer not null references employees(e_id)
);
