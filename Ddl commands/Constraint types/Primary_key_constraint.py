"""PRIMARY KEY CONSTRAINT принуждает стобец(цы) содержать только уникальные значения
 и не разрешает содержать значение NULL.В таблице не может больше одного столбца с PRIMARY KEY."""


"""INLINE LEVEL"""
# CREATE TABLE students(
# id number CONSTRAINT st_id_pk PRIMARY KEY,
# name varchar2(15),
# course number,
# faculty_id integer
# );

# CREATE TABLE students(
# id number  PRIMARY KEY,
# name varchar2(15),
# course number,
# faculty_id integer
# );

"""TABLE LEVEL"""

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# CONSTRAINT pk PRIMARY KEY (id)
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# PRIMARY KEY (id)
# );

"""Создать  CONSTRAINT PRIMARY KEY после создание таблицы."""

# ALTER TABLE students MODIFY (id PRIMARY KEY);

# ALTER TABLE students MODIFY (id  CONSTRAINT pk PRIMARY KEY);

# ALTER TABLE students ADD CONSTRAINT pk PRIMARY KEY (id);

