"""INSERT INTO table_name
        column(s)
        SUBQUERY;"""

# INSERT INTO new_emps (emp_id, name, start_date)
# (SELECT employee_id, first_name, hire_date FROM employees WHERE employee_id > 200);

# INSERT INTO new_emps
# (SELECT employee_id, first_name, hire_date, job_id FROM employees WHERE employee_id > 200);
