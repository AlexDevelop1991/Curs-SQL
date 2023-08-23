"""MULTIPLE_ROW_SUBQUERY"""

# SELECT first_name, last_name, salary FROM employees
# WHERE job_id IN (SELECT job_id FROM jobs WHERE min_salary > 8000);

# SELECT first_name, last_name, salary FROM employees
# WHERE job_id NOT IN (SELECT job_id FROM jobs WHERE min_salary > 8000); ---> NOT IN не использовать если есть NULL.

# SELECT first_name, last_name, salary FROM employees
# WHERE job_id IN (SELECT job_id FROM jobs WHERE job_id = 'AD_VP');

# SELECT first_name, last_name, salary FROM employees
# WHERE salary > ANY (SELECT salary FROM employees WHERE department_id = 100); ---> ANY это любой.

# SELECT first_name, last_name, salary FROM employees
# WHERE salary > ALL (SELECT salary FROM employees WHERE department_id = 100); ---> ALL это все.

# SELECT department_name FROM departments
# WHERE department_id IN (SELECT DISTINCT department_id FROM employees);

#