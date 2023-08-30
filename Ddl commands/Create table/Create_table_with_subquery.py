"""CREATE TABLE schema.table
            AS
        subquery"""

# CREATE TABLE new_emps2 AS
# (SELECT employee_id, first_name, last_name, salary, department_id FROM employees);

# CREATE TABLE new_dep AS
# (SELECT department_name, MAX(salary) max_salary, MIN(salary) min_salary
# FROM employees e JOIN departments d
# ON(e.department_id = d.department_id) GROUP BY department_name);

# CREATE TABLE new_regions AS (SELECT * FROM regions WHERE 5 = 6);

