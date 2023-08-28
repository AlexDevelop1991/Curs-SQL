"""1. Перепишите и запустите данный statemenet для создания таблицы
locations2, которая будет содержать такие же столбцы, что и locations:
CREATE TABLE locations2 AS (SELECT * FROM locations WHERE 1=2);"""
# CREATE TABLE locations2 AS (SELECT * FROM locations WHERE 1=2);

"""2. Добавьте в таблицу locations2 2 строки с информацией о id локации,
адресе, городе, id страны. Пусть данные строки относятся к стране Италия."""
"""3. Совершите commit."""
# INSERT INTO locations2 (location_id, street_address, city, country_id)
# (SELECT location_id, street_address, city, country_id FROM locations WHERE country_id = 'IT');
# COMMIT;

"""4. Добавьте в таблицу locations2 ещё 2 строки, не используя
перечисления имён столбцов, в которые заносится информация. Пусть
данные строки относятся к стране Франция. При написании значений,
где возможно, используйте функции."""
"""5. Совершите commit."""
# INSERT INTO locations2
# VALUES (1000 + 200, INITCAP('bila bongo street'), null, 'Paris', null, UPPER('fr'));
# INSERT INTO locations2
# VALUES (3000 / 2, CONCAT('34509 ', 'Viva La Paris'), null, INITCAP('leon'),null, 'FR');
# COMMIT;

"""6. Добавьте в таблицу locations2 строки из таблицы locations, в которых
длина значения столбца state_province больше 9."""
"""7. Совершите commit."""
# INSERT INTO locations2 (location_id, street_address, city, country_id)
# (SELECT location_id, street_address, city, country_id FROM locations WHERE LENGTH(state_province) > 9);
# COMMIT;

