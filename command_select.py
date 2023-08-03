                    ### Команда SELECT ###

"""3 фундаментальные концепции"""
# PROJECTION - выбор столбцов из таблицы.
# SELECTION - выбор строк из таблицы.
# JOINING - объединения таблиц.

"""SELECT statement(не меняет данные)
        Basic syntax"""
# SELECT * FROM table; ---> SELECT * FROM countries;
# SELECT column(s) FROM table; ---> SELECT country_name FROM countries;

"""SELECT statement(не меняет данные)
        DISTINCT"""
# DISTINCT - выводит только уникальные значения
# SELECT DISTINCT column(s) FROM table; ---> SELECT DISTINCT job_id FROM job_history;

"""SELECT statement(не меняет данные)
        EXpressions in select list"""
# SELECT column(s), expression(s) FROM table; ---> SELECT salary*2 FROM employees;
# CONCATENATE - объединяет строки (используют так ||), можно объединять не только текстовые колонки.

"""SELECT statement(не меняет данные)
        ALIAS"""
# Alias - это альтернативное имя для столбца или целого выражения.
# SELECT column(s) alias, expression(s) alias FROM table; ---> SELECT salary*2 AS bonus FROM employees;
# ---> SELECT start_date start, end_date end,(end_fate - start_date)+1 "Count Of Days" FROM job_history;
# ---> select 'My name is ' || first_name || ' and my last name is ' || last_name  our_employees from employees;

"""SELECT statement(не меняет данные)
        Таблица DUAL"""
# SELECT 'privet,' || 'dorogoy student' AS greeting FROM dual;

"""Проблемы с одинарными кавычками в тексте"""
# Решение --> SELECT 'It''s my life' AS song FROM dual;
# Quote(q) оператор:
# q'delimiter нащ текст с кавычками delimiter'
# SELECT q'<It's my life>' AS song FROM dual;

"""SELECT statement(не меняет данные)
Итог первого знакомства с SELECT"""
# SELECT * |{DISTINCT column(s) alias, expression(s) alias} FROM table;


