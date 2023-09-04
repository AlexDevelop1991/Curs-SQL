# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer REFERENCES faculties ON DELETE CASCADE --> Значит если удалить в одной таблицы то в другой удаляться все строки связанны по ID.
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer REFERENCES faculties ON DELETE SET NULL --> При удалении с одной таблицы в другой таблицы значения которые сязывали таблицы будет NULL.
# );

