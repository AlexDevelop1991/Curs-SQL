"""MERGE INTO table_name1 t1
USING {table_name2 | subquery} t2
ON (t1.column = t2.column)
WHEN MATCHED THEN
UPDATE SET column = value
DELETE WHERE condition
WHEN NOT MATCHED THEN
INSERT (value1, value2)
VALUES (column1, column2);"""

# MERGE INTO new_emps ne
# USING employees e
# ON(ne.emp_id = e.employee_id)
# WHEN MATCHED THEN
# UPDATE SET ne.start_date = SYSDATE
# DELETE WHERE ne.job LIKE '%IT%'
# WHEN NOT MATCHED THEN
# INSERT (emp_id, name, start_date, job)
# VALUES (employee_id, last_name, hire_date, job_id);
