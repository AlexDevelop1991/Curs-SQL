"""1. Создать таблицу friends с помощью subquery так, чтобы она после
создания содержала значения следующих столбцов из таблицы
employees: employee_id, first_name, last_name для тех строк, где
имеются комиссионные. Столбцы в таблице friends должны называться
id, name, surname ."""
# CREATE TABLE friends
# AS
# (SELECT employee_id id, first_name name, last_name surname FROM employees WHERE commission_pct is not null);

"""2. Добавить в таблицу friends новый столбец email ."""
# ALTER TABLE friends
# ADD (email VARCHAR2(30));

"""3. Изменить столбец email так, чтобы его значение по умолчанию было «no email»."""
# ALTER TABLE friends
# MODIFY (email VARCHAR2(30) DEFAULT 'No email');

"""4. Проверить добавлением новой строки, работает ли дефолтное значение столбца email."""
# INSERT INTO friends (id, name, surname)
# VALUES (40, 'Alex', 'Brovco');

"""5. Изменить название столбца с id на friends_id ."""
# ALTER TABLE friends
# RENAME COLUMN id TO friends_id;

"""6. Удалить таблицу friends."""
# DROP TABLE friends;

"""7. Создать таблицу friends со следующими столбцами: id, name, surname,
email, salary, city, birthday. У столбцов salary и birthday должны быть значения по умолчанию."""
# CREATE TABLE friends (
# id INTEGER,
# name VARCHAR2(15),
# surname VARCHAR2(15),
# email VARCHAR2(30),
# salary INTEGER DEFAULT 1000,
# city VARCHAR2(15),
# birthday DATE DEFAULT ROUND(SYSDATE)
# );

"""8. Добавить 1 строку в таблицу friends со всеми значениями."""
# INSERT INTO friends (id, name, surname, email, salary, city, birthday)
# VALUES (1, 'Alex', 'Brovco', 'stars1991@gmail.com', 10000, 'Kishinev', TO_DATE('16-AUG-91', 'DD-MON-YYYY'));

"""9. Добавить 1 строку в таблицу friends со всеми значениями кроме salary и birthday."""
"""10.Совершить commit."""
# INSERT INTO friends (id, name, surname, email, city)
# VALUES (2, 'Marina', 'Sirghi', 'marinka@gmail.com', 'Moscow');
# COMMIT;

"""11.Удалить столбец salary."""
# ALTER TABLE friends
# DROP COLUMN salary;

"""12.Сделать столбец email неиспользуемым (unused)."""
# ALTER TABLE friends
# SET UNUSED COLUMN email;

"""13.Сделать столбец birthday неиспользуемым (unused)."""
# ALTER TABLE friends
# SET UNUSED COLUMN birthday;

"""14.Удалить из таблицы friends неиспользуемые столбцы."""
# ALTER TABLE friends
# DROP UNUSED COLUMNS;

"""15.Сделать таблицу friends пригодной только для чтения."""
# ALTER TABLE friends READ ONLY;

"""16.Проверить предыдущее действие любой DML командой."""
# DELETE FROM friends WHERE id = 1;

"""17.Опустошить таблицу friends."""
# TRUNCATE TABLE friends;

"""18.Удалить таблицу friends."""
# DROP TABLE friends;