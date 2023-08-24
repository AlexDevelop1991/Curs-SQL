"""SELECT column(s)
FROM table_1
JOIN
table_2
USING(column(s));"""

# SELECT first_name, last_name, salary, department_name,
# e.manager_id emp_manager, d.manager_id dep_manager ,department_id
# FROM employees e
# JOIN departments d
# USING(department_id);

# SELECT * FROM regions JOIN countries USING(region_id);

# SELECT first_name, last_name, jh.job_id, start_date, end_date
# FROM employees
# JOIN job_history jh
# USING(employee_id);
