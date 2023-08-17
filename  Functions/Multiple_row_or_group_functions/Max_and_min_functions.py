"""MIN({DISTINCT | ALL} expression) Игнорирует NULL"""
"""MAX({DISTINCT | ALL} expression) Игнорирует NULL"""

# SELECT MIN(salary), MAX(SALARY) FROM employees;
# SELECT MIN(salary), MAX(SALARY) FROM employees WHERE department_id = 50;
# SELECT MIN(hire_date), MAX(hire_date) FROM employees;
# SELECT MIN(hire_date), MAX(hire_date) FROM employees WHERE department_id = 80;
# SELECT MIN(last_name), MAX(last_name) FROM employees WHERE department_id = 50;
# SELECT MAX(LENGTH(first_name)), MIN(LENGTH(first_name)) FROM employees;

