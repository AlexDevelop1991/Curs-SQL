                    ### INNER JOIN(NATURAL JOIN) ###

## NATURAL JOIN ##               ## USING ##             ## ON ##

"""NATURAL JOIN объединяет таблицы по одинаковому названию столбца."""
"""SELECT column(s)
FROM table_1
NATURAL JOIN
table_2;"""

# SELECT * FROM regions  NATURAL JOIN countries ;

# SELECT c.country_name, c.country_id, r.region_name, region_id
# FROM regions r
# NATURAL JOIN countries c ;

# SELECT first_name, last_name, salary, department_name, department_id, manager_id
# FROM employees
# NATURAL JOIN departments ;

# SELECT c.country_name, c.country_id, r.region_name, region_id
# FROM regions r
# NATURAL JOIN countries c WHERE region_name = 'Europe';
