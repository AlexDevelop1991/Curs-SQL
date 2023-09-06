"""В COMPLEX_VIEW мы не можем делать DML-команды.
1. Можем использовать объединения таблиц.
2. Можем использовать функции.
3. Можем использовать агрегацию."""

# CREATE VIEW fin_emp2 AS SELECT department_name, SUM(salary) sum_salary FROM employees e
# JOIN departments d ON (e.department_id = d.department_id)
# GROUP BY department_name;

# CREATE VIEW v100 AS SELECT SUBSTR(name, 2) name, course FROM students; ---> В этом случаии DELETE проидёт.

# CREATE VIEW v105 AS SELECT DISTINCT name, course FROM students;

# CREATE VIEW v110 AS SELECT ROWNUM r, name, course FROM students;

