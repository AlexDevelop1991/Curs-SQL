# SELECT emp1.employee_id, emp1.first_name, emp1.manager_id, emp2.first_name manager_name
# FROM employees emp1
# JOIN employees emp2
# ON(emp1.manager_id = emp2.employee_id);

# SELECT emp2.first_name manager_name, COUNT(*)
# FROM employees emp1
# JOIN employees emp2
# ON(emp1.manager_id = emp2.employee_id)
# GROUP BY emp2.first_name
# ORDER BY COUNT(*);