BEGIN;
--
-- Create model Department
--
CREATE TABLE "employee_department" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(250) NOT NULL UNIQUE);
--
-- Create model Position
--
CREATE TABLE "employee_position" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(250) NOT NULL UNIQUE);
--
-- Create model Employee
--
CREATE TABLE "employee_employee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "first_name" varchar(25) NOT NULL, "middle_name" varchar(25) NOT NULL, "last_name" varchar(25) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "gender" varchar(25) NOT NULL, "birth_date" date NOT NULL, "monthly_salary" decimal NOT NULL, "active" bool NOT NULL, "department_id" integer NOT NULL REFERENCES "employee_department" ("id") DEFERRABLE INITIALLY DEFERRED, "position_id" integer NOT NULL REFERENCES "employee_position" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "employee_employee_department_id_8fce1a05" ON "employee_employee" ("department_id");
CREATE INDEX "employee_employee_position_id_7083276e" ON "employee_employee" ("position_id");
COMMIT;
