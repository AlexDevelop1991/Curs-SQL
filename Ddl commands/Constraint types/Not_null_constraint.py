"""NOT NULL CONSTRAINT не разрешает столбцам содержать значение NULL"""

"""CONSTRAINT NOT NULL нельзя сделать сразу на нестолько столбцов."""

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number CONSTRAINT stud_course_notnull NOT NULL,
# faculty_id integer
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number  NOT NULL,
# faculty_id integer
# );

"""Создать  CONSTRAINT NOT NULL после создание таблицы."""

# ALTER TABLE students MODIFY (course CONSTRAINT st_course_notnull NOT NULL);

# ALTER TABLE students MODIFY (course  NOT NULL);

"""Убрать CONSTRAINT NOT NULL после создание таблицы."""

# ALTER TABLE students MODIFY (course NULL);

