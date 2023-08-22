"""1. Выведите информацию о регионах и количестве сотрудников в каждом регионе."""
#

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
#