"""COUNT({ * | {DISTINCT | ALL} expression}) Игнорирует NULL"""

# SELECT COUNT(*) FROM employees;
# SELECT COUNT(*) FROM employees WHERE salary > 5000;
# SELECT COUNT(salary) FROM employees; ---> 107.
# SELECT COUNT(commission_pct) FROM employees; ---> 35.
# SELECT COUNT(NVL(commission_pct, 0)) FROM employees; ---> 107.
# SELECT COUNT(DISTINCT commission_pct) FROM employees; ---> 7.
# SELECT COUNT(first_name), COUNT(DISTINCT first_name) FROM employees;
# SELECT COUNT('abc') FROM employees; рядом с каждой строкой появиться 'abc' получаеться из будет столько сколько строк в таблице.
