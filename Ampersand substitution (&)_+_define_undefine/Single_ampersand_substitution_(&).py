"""SINGLE AMPERSAND SUBSTITUTION (&) работает как в SELECT так и в любых DML-командах."""
"""SINGLE AMPERSAND SUBSTITUTION (&) ещё называют RUNTIME BINDING."""
# SELECT first_name, last_name, salary
# FROM employees
# WHERE employee_id = 130;

# SELECT first_name, last_name, salary
# FROM employees
# WHERE employee_id = &ID; --> Таким образом ORACLE сам будет спрасивать вас параметр переменной(используют для частых SELECT)

# SELECT first_name, last_name, salary
# FROM employees
# WHERE first_name = '&name'; --> при работе с текстом ставим кавычки чтоб при запросе их не писать.

# SELECT first_name, last_name, salary
# FROM employees
# WHERE first_name = '&name'
# AND salary > &sal;