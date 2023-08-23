# SELECT first_name, last_name, salary FROM employees
# WHERE department_id IN (SELECT department_id FROM departments
# WHERE location_id IN (SELECT location_id FROM locations
# WHERE country_id  = (SELECT country_id FROM countries WHERE country_name = 'United Kingdom')));

# SELECT first_name, last_name, salary FROM employees
# WHERE job_id IN (SELECT job_id FROM jobs WHERE UPPER(job_title) LIKE '%MANAGER%')
# AND salary > (SELECT AVG(salary) FROM employees);

# SELECT first_name, last_name, salary FROM employees
# WHERE salary > (SELECT MAX(salary) FROM employees WHERE first_name = 'David');
