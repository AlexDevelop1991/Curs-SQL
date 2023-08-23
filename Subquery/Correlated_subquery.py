"""CORRELATED_SUBQUERY(коррелированный подзапрос)"""

# SELECT e1.first_name, e1.last_name, e1.salary FROM employees e1
# WHERE salary > (SELECT AVG(e2.salary) FROM employees e2
# WHERE e2.department_id = e1.department_id);