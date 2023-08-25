"""UPDATE table_name
        SET
column(s) = subquery(s)
WHERE column = subquery;"""

# UPDATE employees SET salary = 5000 WHERE department_id =
# (SELECT department_id FROM departments WHERE department_name = 'Marketing');

# UPDATE employees SET salary = (SELECT MAX(salary) FROM employees),
# hire_date = (SELECT MIN(start_date) FROM job_history)
# WHERE employee_id = 180;

# 