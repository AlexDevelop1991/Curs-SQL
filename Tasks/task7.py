"""1. Выведите информацию о регионах и количестве сотрудников в каждом регионе."""
# SELECT region_name, COUNT(*)
# FROM employees e
# JOIN departments d
# ON(e.department_id = d.department_id)
# JOIN locations l
# ON(d.location_id = l.location_id)
# JOIN countries c
# ON(l.country_id = c.country_id)
# JOIN regions r
# ON(c.region_id = r.region_id)
# GROUP BY region_name;

"""2. Выведите детальную информацию о каждом сотруднике: имя,
фамилия, название департамента, job_id, адрес, страна и регион."""
# SELECT first_name, last_name, department_name, job_id, street_address, country_name, region_name
# FROM employees e
# JOIN departments d
# ON(e.department_id = d.department_id)
# JOIN locations l
# ON(d.location_id = l.location_id)
# JOIN countries c
# ON(l.country_id = c.country_id)
# JOIN regions r
# ON(c.region_id = r.region_id);

"""3. Выведите информацию о имени менеджеров которые имеют в подчинении больше 6ти сотрудников, 
а также выведите количество сотрудников, которые им подчиняются."""
# SELECT emp2.first_name manager_name, COUNT(*)
# FROM employees emp1
# JOIN employees emp2
# ON(emp1.manager_id = emp2.employee_id)
# GROUP BY emp2.first_name
# HAVING COUNT(*) > 6;

"""4. Выведите информацию о названии всех департаментов и о количестве
работников, если в департаменте работают больше 30ти сотрудников.
Используйте технологию «USING» для объединения по id
департамента."""
# SELECT department_name, COUNT(*)
# FROM employees
# JOIN departments
# USING(department_id)
# GROUP BY department_name
# HAVING COUNT(*) > 30;

"""5. Выведите названия всех департаментов, в которых нет ни одного сотрудника."""
# SELECT department_name
# FROM employees e
# RIGHT OUTER JOIN departments d
# ON(e.department_id = d.department_id)
# WHERE first_name IS NULL;

"""6. Выведите всю информацию о сотрудниках, менеджеры которых
устроились на работу в 2005ом году, но при это сами работники
устроились на работу до 2005 года."""
# SELECT * FROM employees emp1
# JOIN employees emp2
# ON(emp1.manager_id= emp2.employee_id)
# WHERE TO_CHAR(emp2.hire_date, 'YYYY') = '2005'
# AND emp1.hire_date < TO_DATE('01-01-2005', 'DD-MM-YYYY');

"""7. Выведите название страны и название региона этой страны, используя natural join."""
# SELECT c.country_name, r.region_name
# FROM countries c
# NATURAL JOIN regions r;

"""8. Выведите имена, фамилии и з/п сотрудников, которые получают
меньше, чем (минимальная з/п по их специальности + 1000)."""
# SELECT first_name, last_name, salary
# FROM employees e
# JOIN jobs j
# ON(e.job_id = j.job_id AND salary < min_salary + 1000);

"""9. Выведите уникальные имена и фамилии сотрудников, названия стран,
в которых они работают. Также выведите информацию о сотрудниках,
о странах которых нет информации. А также выведите все страны, в
которых нет сотрудников компании."""
# SELECT DISTINCT first_name, last_name, country_name
# FROM employees e
# FULL OUTER JOIN departments d
# ON(e.department_id = d.department_id)
# FULL OUTER JOIN locations l
# ON(d.location_id = l.location_id)
# FULL OUTER JOIN countries c
# ON(l.country_id = c.country_id);

"""10.Выведите имена и фамилии всех сотрудников, а также названия стран,
которые мы получаем при объединении работников со всеми
странами без какой-либо логики."""
# SELECT first_name, last_name, country_name
# FROM employees
# CROSS JOIN countries;

"""11.Решите задачу № 1, используя Oracle Join синтаксис."""
# SELECT region_name, COUNT(*)
# FROM employees e, departments d, locations l, countries c, regions r
# WHERE e.department_id = d.department_id AND d.location_id = l.location_id
# AND l.country_id = c.country_id AND c.region_id = r.region_id
# GROUP BY region_name;

"""12.Решите задачу № 5, используя Oracle Join синтаксис."""
# SELECT department_name
# FROM employees e, departments d
# WHERE e.department_id(+) = d.department_id AND  first_name IS NULL;
