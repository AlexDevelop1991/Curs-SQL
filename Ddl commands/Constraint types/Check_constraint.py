"""CHECK CONSTRAINT принуждает использовать только значения которые удовлетворяют его условию(ям)"""

"""INLINE LEVEL"""
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number CONSTRAINT ch CHECK (course > 0 AND course < 6),
# faculty_id integer
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# email varchar2(15) CHECK (INSTR(email, '@') > 0), --> Значит что email должен содержать собачку(@).
# faculty_id integer
# );

"""TABLE LEVEL"""
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# CONSTRAINT ch CHECK (course > 0 AND course < 6)
# );

"""Создать  CHECK CONSTRAINT после создание таблицы."""

# ALTER TABLE students MODIFY (id CONSTRAINT ch CHECK (id >= 1));

# ALTER TABLE students MODIFY (id CHECK (id >= 1));

# ALTER TABLE students ADD CONSTRAINT ch2 CHECK (course < 20);

#