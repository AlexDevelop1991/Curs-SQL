"""SUM({DISTINCT | ALL} expression) Игнорирует NULL"""

# SELECT SUM(salary) FROM employees;
# SELECT SUM(salary), SUM(DISTINCT salary) FROM employees;
# SELECT SUM(commission_pct) FROM employees;
# SELECT SUM(DISTINCT commission_pct) FROM employees;
# SELECT SUM('7') FROM employees; к каждой строке добавляеться 7 а строк 107 значит 7 * 107 = 749.
# SELECT ROUND(SUM(SYSDATE - hire_date ) / 365) FROM employees; это сколько лет в сумме проработали работники на сегодняшний день.
# SELECT SUM(LENGTH(first_name)) FROM employees;

