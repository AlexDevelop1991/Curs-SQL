"""Самый нормальный лучше его использовать"""
"""SELECT column(s)
FROM table_1
JOIN
table_2
ON(column1 = column2)"""

# SELECT first_name, last_name, jh.job_id, start_date, end_date
# FROM employees
# JOIN job_history jh
# ON(employees.employee_id = jh.employee_id);

# SELECT * FROM departments JOIN regions ON(region_id * 10 = department_id);

# SELECT first_name, last_name, jh.job_id, start_date, end_date
# FROM employees e
# JOIN job_history jh
# ON(e.employee_id = jh.employee_id AND e.department_id = jh.department_id);

# SELECT first_name, department_name FROM employees JOIN departments
# ON(employees.employee_id = departments.manager_id);
