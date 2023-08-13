                    ### General Functions ###
"""NVL(value,ifnull) принимает 2 обязательных параметра функция работает с NULL"""
# SELECT first_name, NVL(commission_pct, 0) FROM employees;

"""NVL2(value,ifnotnull,ifnull) принимает 3 обязательных параметра"""
"""Первый параметр никогда не возвращает,второй возвращает если первый NOT NULL,и возвращает третий если первый NULL.
типы данных второго и третьего параметра должны быть одинаковы или совместимы и они не могут быть типа данных LONG."""
# SELECT NVL2(17, 18, 19) FROM dual;
# SELECT NVL2(NULL, 18, 19) FROM dual;
# SELECT first_name, NVL2(commission_pct, commission_pct, 0) FROM employees;
# SELECT first_name, NVL2(commission_pct, 'Yes commission', 'No commission') FROM employees;

"""NULLIF(value1,value2) NULL если, принимает два обязательных параметра, эта функция возвращает NULL если первый и
второй параметры равны между собой,и возвращает первый параметр есои первый не равен второму параметру"""
# SELECT NULLIF(18, 18) FROM dual;
# SELECT NULLIF(17, 18) FROM dual;
# SELECT NULLIF('18-SEP-87', '18/SEP/87') FROM dual;
# SELECT NULLIF(TO_DATE('18-SEP-87'), TO_DATE('18/SEP/87')) FROM dual;
# SELECT country_id, country_name, NVL2(NULLIF(country_id, UPPER(SUBSTR(country_name, 1, 2))), 'Nesovpadeniia', 'Sovpadeniia') FROM countries;

"""COALESCE(value1,value2,...,valueN) принимает минимум 2 параметра то 2 параметра обязательны ну в принципе можете 
писать сколько хотите параметров,но 2 обязательно.Функция возвращает первое значение которое не NULL со своего параметра
листа,если все параметры значения NULL то функция вернёт NULL."""
# SELECT COALESCE(1, NULL, 2) FROM dual;
# SELECT COALESCE(NULL, NULL, 'ok', 'Hey') FROM dual;
# SELECT first_name, commission_pct, manager_id, salary, COALESCE( commission_pct, manager_id, salary) FROM employees;





