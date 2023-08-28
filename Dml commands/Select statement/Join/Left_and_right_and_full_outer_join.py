"""SELECT column(s) FROM
table_1 LEFT OUTER JOIN table_2
ON(column1 = column2);"""
# SELECT first_name, last_name, salary, department_name
# FROM employees e
# LEFT OUTER JOIN departments d
# ON(e.department_id = d.department_id);

# SELECT first_name, last_name, salary, department_name
# FROM departments d
# LEFT OUTER JOIN employees e
# ON(e.department_id = d.department_id);  Уже будет другой Output.

# SELECT first_name, last_name, salary, department_name
# FROM departments d
# LEFT OUTER JOIN employees e
# ON(e.department_id = d.department_id)
# WHERE department_name LIKE '%i%';

# SELECT department_name, d.department_id
# FROM departments d
# LEFT OUTER JOIN employees e
# ON(e.department_id = d.department_id)
# WHERE e.department_id IS NULL;


"""SELECT column(s) FROM
table_1 RIGHT OUTER JOIN table_2
ON(column1 = column2);"""
# SELECT first_name, last_name, salary, department_name
# FROM employees e
# RIGHT OUTER JOIN departments d
# ON(e.department_id = d.department_id);

# SELECT first_name, last_name, salary, department_name, department_id
# FROM employees
# RIGHT OUTER JOIN departments
# USING(department_id);

# SELECT country_name, city, street_address
# FROM locations l
# RIGHT OUTER JOIN countries c
# ON(l.country_id = c.country_id);


"""SELECT column(s) FROM
table_1 FULL OUTER JOIN table_2
ON(column1 = column2);"""
# SELECT NVL(first_name, 'No employee'), NVL(last_name, 'No employee'),
# NVL(salary,0), NVL(department_name, 'No department')
# FROM employees e
# FULL OUTER JOIN departments d
# ON(e.department_id = d.department_id);
