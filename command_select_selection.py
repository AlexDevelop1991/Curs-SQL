                    ### Концепция Selection ###
# SELECT *|{DISTINCT column(s) alias, expression(s) alias} FROM table WHERE condition(s)
# SELECT first_name, last_name, salary FROM employees WHERE salary >= 10000;
# SELECT first_name, salary FROM employees WHERE last_name = 'King';
# SELECT email FROM employees WHERE hire_date = '21.09.05';
# SELECT * FROM employees WHERE employee_id = manager_id+1000/10+1;
# SELECT * FROM job_history WHERE start_date+364 = end_date;

"""SELECT Операторы сравнения"""
# = равно
# <, >  больше или меньше
# <=, >= больше или равно, меньше или равно
# !=, <> Не равно
# SELECT first_name, last_name, salary FROM employees WHERE salary >= (10000-1500)*2;
# SELCT * FROM employees WHERE first_name < 'Kevin';
# SELECT * FROM job_history WHERE start_date < '01.01.05';

"""Оператор BETWEEN(между) начальный и конечный парамметр включенны чаще всего используют для дат и чисел, строк можно но не рекомендуется."""
# SELECT first_name, last_name, salary FROM employees WHERE salary BETWEEN 4000 and 10000;
# SELECT first_name, last_name, salary FROM employees WHERE salary <= 4000 and salary <= 10000; (вместо BETWEEN)
# SELECT * FROM job_history WHERE start_date BETWEEN '01.01.05' and '01.01.10';
# SELECT * FROM employees WHERE first_name BETWEEN 'A' and 'C';

""" Оператор IN(в, внутри):"""
# SELECT * FROM departments WHERE location_id IN (1700, 1500, 2400);
# SELECT * FROM departments WHERE location_id=1700 OR location_id=1500 OR location_id=2400; (вместо IN)
# SELECT * FROM job_history WHERE job_id IN ('IT_PROG', 'ST_CLERK');
# SELECT * FROM job_history WHERE start_date IN ('13.01.01', '01.01.10');

"""Оператор IS NULL(проверяет на NULL)"""
# SELECT * FROM employees WHERE commission_pct IS NULL;

"""Операто LIKE( %, _) (работает только с текстовым типом и предоставляет очень мощный механизм для поиска и сравнения.)"""
#  Специальный символ для LIKE (%) - на 0 или больше количество символов.
#  Специальный символ для LIKE (_)- ровно на один любой символ.
# SELECT * FROM employees WHERE first_name LIKE 'S%'; - имя которое начинаеться на 'S', a % говорит что после 'S' может быть любое кол-во букв или символов.
# SELECT * FROM employees WHERE first_name LIKE '%r'; - имя заканчивает на букву 'r'
# SELECT * FROM employees WHERE first_name LIKE 'A%r'; - первая буква A, последня r, между ними не важно что.
# SELECT * FROM employees WHERE first_name LIKE 'D_n'; _ - заменяет только один символ или одну букву.
# SELECT * FROM employees WHERE first_name LIKE 'St_v_n';
# SELECT * FROM employees WHERE job_id LIKE 'ST\_%' ESCAPE '\'; - ESCAPE '\' после себя делает символ _ обычным, то есть снимает с _ специальный символ.

"""SELECT Логические операторы"""
"""AND(и)"""
# Всё выражения примает значение TRUE тогда и только тогда,когда все объединненые условия AND,по отдельнности тоже возвращают TRUE.
# SELECT * FROM employees WHERE first_name LIKE 'D%' AND salary > 10000;
# SELECT * FROM employees WHERE first_name LIKE 'D%' AND salary BETWEEN 4000 AND 10000;



