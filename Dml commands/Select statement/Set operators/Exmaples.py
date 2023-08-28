# SELECT first_name, salary FROM employees WHERE first_name LIKE '%a%'
# INTERSECT
# SELECT first_name, salary FROM employees WHERE first_name LIKE '%e%'
# MINUS
# SELECT first_name, salary FROM employees WHERE first_name LIKE '%l%';

# SELECT first_name, salary FROM employees WHERE first_name LIKE '%a%'
# UNION
# SELECT first_name, salary FROM employees WHERE first_name LIKE '%e%'
# MINUS
# SELECT first_name, salary FROM employees WHERE first_name LIKE '%l%';

# SELECT first_name, salary FROM employees WHERE first_name LIKE '%a%'
# UNION
# (SELECT first_name, salary FROM employees WHERE first_name LIKE '%e%'
# MINUS
# SELECT first_name, salary FROM employees WHERE first_name LIKE '%l%');

# SELECT manager_id FROM employees WHERE department_id = 20
# INTERSECT
# SELECT manager_id FROM employees WHERE department_id = 30;

# SELECT department_id dep_id, to_char(null) job_id, SUM(salary) FROM employees
# GROUP BY department_id
# UNION
# SELECT to_number(null), job_id, SUM(salary) FROM employees
# GROUP BY job_id;

