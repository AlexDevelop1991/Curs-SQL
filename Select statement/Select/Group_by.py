"""SELECT * |{DISTINCT column(s) alias, expression(s) alias,
group_f-on(s) (column(s) | expression(s) alias),}
FROM table
WHERE condition(s)
GROUP BY {column(s) | expression(s)}
ORDER BY {column(s) | expression(s) | numeric position}
{ASC | DESC}{NULLS FIRST | LAST};"""

# ASC - это по возрастанию (идёт по default)
# DESC - это по убыванию
# NULL FIRST или LAST - указывает в сортировке как будет выводть NULL в начале или в конце.

# SELECT department_id, COUNT(*) FROM employees GROUP BY department_id ORDER BY 1, 2;
# SELECT department_id, COUNT(*), MIN(salary), MAX(salary) FROM employees GROUP BY department_id ORDER BY 1, 2;
# SELECT department_id, manager_id, COUNT(*) FROM employees GROUP BY department_id, manager_id ORDER BY 1, 2, 3;
# SELECT job_id, MIN(salary), MAX(salary) FROM employees GROUP BY job_id;

# SELECT job_id, MIN(salary), MAX(salary), ROUND(AVG(salary)) FROM employees
# WHERE LENGTH(first_name) > 4 AND salary > 5000
# GROUP BY job_id
# ORDER BY AVG(salary);

# SELECT MAX(hire_date), MIN(first_name), COUNT(*), AVG(salary), SUM(employee_id)
# FROM employees
# GROUP BY department_id;

# SELECT TO_CHAR(hire_date, 'Month'), COUNT(*) FROM employees GROUP BY TO_CHAR(hire_date, 'Month');
# SELECT department_id, job_id, COUNT(*) FROM employees GROUP BY department_id, job_id ORDER BY department_id;

# SELECT job_id, TO_CHAR(hire_date, 'yyyy') year, COUNT(*), SUM(salary) FROM employees
# WHERE job_id IN ('ST_CLERK','SA_REP','SH_CLERK') AND employee_id > 115
# GROUP BY job_id, TO_CHAR(hire_date, 'yyyy')
# ORDER BY job_id, year;

"""GROUP BY WITH HAVING(Ограничивает)"""
"""SELECT * |{DISTINCT column(s) alias, expression(s) alias,
group_f-on(s) (column(s) | expression(s) alias),}
FROM table
WHERE condition(s)
GROUP BY {column(s) | expression(s)}
HAVING group_condition(s)
ORDER BY {column(s) | expression(s) | numeric position}
{ASC | DESC}{NULLS FIRST | LAST};"""

# SELECT department_id, COUNT(*) FROM employees
# WHERE LENGTH(first_name) > 4
# GROUP BY department_id
# HAVING COUNT(*) > 3
# ORDER BY department_id;

# SELECT department_id, COUNT(*), ROUND(AVG(salary)) FROM employees
# WHERE LENGTH(first_name) > 4 AND employee_id > 10
# GROUP BY department_id
# HAVING COUNT(*) > 3 AND  ROUND(AVG(salary)) > 5000
# ORDER BY department_id;



