"""UNIQUE принуждает столбец(цы) содержать только уникальные значения.Исключение только - NULL."""

"""INLINE LEVEL"""
# CREATE TABLE students(
# id number CONSTRAINT st_id_unique UNIQUE,
# name varchar2(15),
# course number,
# faculty_id integer,
# avg_score number(5, 2),
# start_date date,
# scholarship integer
# );

"""TABLE LEVEL"""
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# avg_score number(5, 2),
# start_date date,
# scholarship integer,
# CONSTRAINT st_id_unique UNIQUE (id)
# );

"""COMPOSITE CONSTRAINT для нескольких столбцов."""
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# avg_score number(5, 2),
# start_date date,
# scholarship integer,
# CONSTRAINT st_id_unique UNIQUE (id, name)
# );

"""Добавление CONSTRAINT после создания таблицы."""
# ALTER TABLE students ADD CONSTRAINT st_id_unique UNIQUE (id);

# ALTER TABLE faculties ADD  UNIQUE (id);

# ALTER TABLE students MODIFY (id CONSTRAINT abc UNIQUE);

# ALTER TABLE faculties MODIFY (id  UNIQUE);

"""Удаление CONSTRAINT после создания таблицы."""

# ALTER TABLE students DROP CONSTRAINT abc;

