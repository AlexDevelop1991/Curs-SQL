"""SELECT ORDER BY(упорядочить,сортировать)"""

"""SELECT * |{DISTINCT column(s) alias, expression(s) alias}
FROM table WHERE condition(s)
ORDER BY{column(s) | expression(s) | numeric position}
{ASC | DESC}{NULLS FIRST | LAST};"""
# ASC - это по возрастанию (идёт по default)
# DESC - это по убыванию
# NULL FIRST или LAST - указывает в сортировке как будет выводть NULL в начале или в конце.

# SELECT first_name, salary FROM employees ORDER BY salary; ---> по возрастанию
# SELECT first_name, salary FROM employees  ORDER BY salary DESC; ---> по убыванию
# SELECT first_name, salary FROM employees WHERE job_id = 'IT_PROG' ORDER BY salary;
# SELECT first_name, salary, hire_date FROM employees WHERE job_id = 'IT_PROG' ORDER BY hire_date;
# SELECT first_name, salary FROM employees  ORDER BY 2; ---> чтоб не писать название столбца мы можем передать его порядковый номер в SELECT листе.
# SELECT job_id, first_name, last_name, salary, hire_date FROM employees ORDER BY job_id DESC, last_name, 4 DESC;


