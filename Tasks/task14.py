"""1. Создать таблицу test200 со следующими столбцами: id, name1, name2,
address1, address2. 1-ый должен быть типа integer, остальные - varchar2."""
# CREATE TABLE test200 (
# id number,
# name1 varchar2(15),
# name2 varchar2(15),
# address1 varchar2(20),
# address2 varchar2(20)
# );

"""2. Напишите такой шаблон для изменения строк, который при каждом
запуске будет спрашивать, значение какого столбца меняется, на какое
значение меняется и для какого значения id меняется."""
# UPDATE test200 SET &col = &val WHERE id = &ID;

"""3. Напишите select, в котором требуется вывести всю информацию из
таблицы test200 для строк, у которых столбцы name1 и name2 равны
одному и тому же значению, а также столбцы address1 и address2 тоже
равны одному и тому же значению. Напишите такой шаблон для этого
statement-а, который при запуске один раз спросит всего 2 значения –
одно для первых 2х столбцов и второе для других 2х столбцов."""
# SELECT * FROM test200
# WHERE name1 = '&&val'
# AND name2 ='&val1'
# AND address1 = '&&adres2'
# AND address2 = '&adres2';

"""Напишите команду/ды, которая удаляет сессионные значения для наших переменных."""
# UNDEFINE val AND adres2;