"""ALTER TABLE table_name
ADD (column_name data_type DEFAULT expr);"""

# ALTER TABLE students ADD (course NUMBER DEFAULT 3);

"""ALTER TABLE table_name
MODIFY (column_name data_type DEFAULT expr);"""

# ALTER TABLE students MODIFY (avg_scoore NUMBER(5,3));

# ALTER TABLE students MODIFY (start_date date DEFAULT NULL);

"""ALTER TABLE table_name
DROP COLUMN column_name;"""

# ALTER TABLE students DROP COLUMN scholarship;

"""ALTER TABLE table_name
SET UNUSED COLUMN column_name;"""

"""ALTER TABLE table_name DROP UNUSED COLUMNS;"""

# ALTER TABLE students SET UNUSED COLUMN start_date;

# ALTER TABLE students DROP UNUSED COLUMNS;

"""ALTER TABLE table_name
RENAME COLUMN column_name1 TO column_name2;"""

# ALTER TABLE students
# RENAME COLUMN student_id TO id;

"""ALTER TABLE table_name READ ONLY;"""

# ALTER TABLE students READ ONLY; ---> Теперь для таблицы можно использовать только SELECT.

