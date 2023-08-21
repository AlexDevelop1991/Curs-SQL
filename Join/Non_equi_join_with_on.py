"""SELECT column(s)
FROM table_1
JOIN
table_2
ON(column1 {оператор неравенства} column2);"""

# SELECT first_name, salary, min_salary, max_salary
# FROM employees e
# JOIN jobs j
# ON(e.job_id = j.job_id AND salary * 2 < max_salary);

# SELECT first_name, salary, min_salary, max_salary
# FROM employees e
# JOIN jobs j
# ON(e.job_id = j.job_id AND salary BETWEEN min_salary + 2000 AND max_salary - 3000);

