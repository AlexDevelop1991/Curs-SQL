"""SUBQUERY(подзапрос)"""
# SELECT first_name, last_name, salary
# FROM employees
# WHERE salary > (SELECT AVG(salary) FROM employees);

# SELECT (SELECT MIN(min_salary) FROM jobs) min_sal,
# (SELECT MAX(LENGTH(first_name)) FROM employees) max_len
# FROM dual;

# SELECT first_name, last_name
# FROM employees
# WHERE employee_id IN (SELECT manager_id FROM employees);

# SELECT department_name, MIN(salary), MAX(salary) FROM
# (SELECT department_name, salary FROM employees e JOIN departments d
# ON(e.department_id = d.department_id))
# GROUP BY department_name;

# SELECT department_name, MIN(salary), MAX(salary) FROM
# (SELECT department_name, salary FROM employees e JOIN departments d
# ON(e.department_id = d.department_id))
# GROUP BY department_name
# HAVING MAX(salary) > (SELECT 2 * 5000 FROM dual)
# AND MIN(salary) < (SELECT salary FROM employees WHERE employee_id = 113);

