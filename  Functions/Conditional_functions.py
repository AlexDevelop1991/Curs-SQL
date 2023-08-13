                    ### Conditional Functions ###
# IF-THEN-ELSE
"""Функция DECODE есть только в ORACLE SQL."""
"""DECODE(exp,comp1,iftrue1,comp2,iftrue2,...compN,iftrueN,iffalse) обязательных 3 параметра,не обязательных может быть сколько угодно."""
"""Если первый параметр равен второму то выводиться третьи параметр."""
# SELECT DECODE(3*4, 12, 'Двенадцать') FROM dual;
# SELECT DECODE(3*4, 15, 'Пятнадцать') FROM dual; ---> NULL
# SELECT DECODE(3*4, 15, 'Пятнадцать', 13, 'Тренадцать', 12, 'Двенадцать') FROM dual;
# SELECT DECODE(3*4, 15, 'Пятнадцать', 13, 'Тренадцать', 16, 'Шестнадцать', 'Нет совпадений') FROM dual; ---> 'Нет совпадений'
# SELECT DECODE(NULL, 12, 'ok', NULL, 'Ravno') FROM dual; ---> 'Ravno'
# SELECT DECODE(2+2*2, 5, 'five', 12/2, 'six1', 6, 'six2') FROM dual; ---> 'six1'
# SELECT first_name, commission_pct, DECODE(commission_pct, NULL, 'No Commission', 0.1, 'Liitle Commission', 0.4, 'Big Commission', 'Middle Commission') AS Commision FROM employees;


                    ### CASE ###
"""Simple Case"""
"""CASE expr
WHEN comp1 THEN iftrue1
WHEN comp2 THEN iftrue2
        .......
WHEN compN THEN iftrueN
ELSE iffalse
END"""
# SELECT CASE 3*4 WHEN 12 THEN 100 END FROM dual;
# SELECT CASE 3*4 WHEN 11 THEN 'eleven' WHEN 12 THEN 'twelve1' WHEN 24/2 THEN 'twelve2' END FROM dual;
# SELECT CASE 3*6 WHEN 11 THEN 'eleven' WHEN 12 THEN 'twelve1' WHEN 24/2 THEN 'twelve2' ELSE 'Not number' END FROM dual;

# SELECT first_name,
# CASE LENGTH(first_name)
# WHEN 4 THEN 'Very short name'
# WHEN 5 THEN 'Short name'
# WHEN 6 THEN 'Middle name'
# WHEN 7 THEN 'Long name'
# WHEN 8 THEN 'Very long name'
# ELSE 'I don''t know'
# END
# AS len_name
# FROM employees;

"""Searched Case"""
"""CASE 
WHEN cond1 THEN iftrue1
WHEN cond2 THEN iftrue2
        .......
WHEN condN THEN iftrueN
ELSE iffalse
END"""
# SELECT CASE  WHEN 3*4=12 THEN 100 END FROM dual;
# SELECT CASE  WHEN 3*4= 11 THEN 'eleven' WHEN 3*4=12 THEN 'twelve1' WHEN 3*4=24/2 THEN 'twelve2' END FROM dual;
# SELECT CASE  WHEN 3*6=11 THEN 'eleven' WHEN 3*6=12 THEN 'twelve1' WHEN 3*6=24/2 THEN 'twelve2' ELSE 'Not number' END FROM dual;

# SELECT first_name, salary, commission_pct,
# CASE
# WHEN LENGTH(first_name) <= 5 THEN 'N1'
# WHEN salary*10 > 100000 THEN 'N2'
# WHEN commission_pct IS NOT NULL THEN 'N3'
# ELSE 'No answer'
# END AS example
# FROM employees;
