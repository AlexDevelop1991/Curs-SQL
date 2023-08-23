"""SINGLE_ROW_SUBQUERY"""

# SELECT first_name, last_name, salary FROM employees
# WHERE salary < (SELECT MAX(salary) / 5 FROM employees);

# SELECT first_name, last_name, salary FROM employees
# WHERE salary > (SELECT AVG(salary) FROM employees);

# SELECT first_name, last_name, salary FROM employees
# WHERE salary >= (SELECT salary FROM employees WHERE employee_id = 180);

# SELECT job_title FROM jobs j JOIN employees e ON(j.job_id = e.job_id)
# GROUP BY job_title
# HAVING AVG(salary) =
# (SELECT MAX(AVG(salary)) FROM employees GROUP BY job_id);

#