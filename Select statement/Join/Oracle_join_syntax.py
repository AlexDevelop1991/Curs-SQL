"""IJ"""
"""SELECT column(s)
FROM table_1 t1, table_2 t2
WHERE t1.column1 = t2.column2;"""

# SELECT first_name, last_name, salary, e.department_id, department_name
# FROM employees e, departments d
# WHERE e.department_id = d.department_id;


"""ROJ"""
"""SELECT column(s)
FROM table_1 t1, table_2 t2
WHERE t1.column1(+) = t2.column2;"""

# SELECT first_name, last_name, salary, e.department_id, department_name
# FROM employees e, departments d
# WHERE e.department_id(+) = d.department_id;


"""LOJ"""
"""SELECT column(s)
FROM table_1 t1, table_2 t2
WHERE t1.column1 = t2.column2(+);"""

# SELECT first_name, last_name, salary, e.department_id, department_name
# FROM employees e, departments d
# WHERE e.department_id = d.department_id(+);

"""CJ"""
"""SELECT column(s)
FROM table_1 t1, table_2 t2;"""

# SELECT * FROM countries, regions;
