"""DELETE
FROM table_name
WHERE column = subquery;"""

# DELETE FROM new_emps WHERE job_id IN
# (SELECT DISTINCT job_id FROM employees WHERE department_id IN
# (SELECT department_id FROM departments WHERE manager_id = 100));

