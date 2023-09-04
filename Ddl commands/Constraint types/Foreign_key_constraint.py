"""FOREIGN KEY CONSTRAINT принуждает использовать только значения
 из опредлённого столбца таблицы-родителя или значения NULL."""

"""INLINE LEVEL"""
# CREATE TABLE faculties(
# id number PRIMARY KEY,
# name varchar2(15)
# );
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer CONSTRAINT st_faculty_fk REFERENCES faculties (id)
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer REFERENCES faculties (id)
# );

"""TABLE LEVEL"""
# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# CONSTRAINT fk FOREIGN KEY (faculty_id) REFERENCES faculties (id)
# );

# CREATE TABLE students(
# id number,
# name varchar2(15),
# course number,
# faculty_id integer,
# FOREIGN KEY (faculty_id) REFERENCES faculties (id)
# );

"""Создать  FOREIGN KEY CONSTRAINT после создание таблицы."""

# ALTER TABLE students MODIFY (CONSTRAINT fk faculty_id REFERENCES faculties(id));

# ALTER TABLE students MODIFY (faculty_id CONSTRAINT fk REFERENCES faculties(id));

# ALTER TABLE students MODIFY (faculty_id REFERENCES faculties(id));

# ALTER TABLE  students ADD CONSTRAINT fk FOREIGN KEY (faculty_id) REFERENCES faculties(id);

# ALTER TABLE  students ADD FOREIGN KEY (faculty_id) REFERENCES faculties(id);

