"""CREATE OR REPLACE {FORCE | NOFORCE} VIEW
 schema.view_name(alias1,alias2,...)
 AS subquery
 WITH CHECK OPTION {CONSTRAINT constrain_name}
 WITH READ ONLY {CONSTRAINT constrain_name};"""

# CREATE OR REPLACE VIEW fin_emp2 AS SELECT * FROM students;

# CREATE FORCE VIEW v200 AS SELECT * FROM students2; ---> FORCE заставляет создать VIEW даже если таблицы не существует.

# CREATE FORCE VIEW v205 AS SELECT * FROM students WHERE course > 2 WITH CHECK OPTION;

# CREATE FORCE VIEW v210 AS SELECT * FROM students WITH READ ONLY;

# CREATE FORCE VIEW v215(id_student, name_student, num_course) AS SELECT * FROM students;

