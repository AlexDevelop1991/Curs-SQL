                    ### Character Function ###
"""Case conversion functions - функции которые работаюм с регистром букв."""\
# LOWER(s) принимает 1 параметр где (s) это строка,текст (выводить текст,строку маленькими буквами).
# SELECT first_name, LOWER(first_name) FROM employees;
# SELECT * FROM employees WHERE LOWER(first_name) = 'david';
# SELECT * FROM employees WHERE LOWER(first_name) LIKE '%en%';
# SELECT LOWER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;

# UPPER(s) примает 1 параметр где (s) это строка,текст (выводит текст,строку большими буквами).
# SELECT first_name, UPPER(first_name) FROM employees;
# SELECT * FROM employees WHERE UPPER(first_name) LIKE '%EN%';
# SELECT UPPER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;

# INITCAP(s) принимает 1 параметр где (s) это строка,текст (В каждос слове делает первую букву заглавной(большой) а остальные маленькие.
# SELECT INITCAP('PRIVET kak dElA?888') FROM dual;
# SELECT INITCAP('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;
# SELECT * FROM employees WHERE INITCAP(first_name) = 'David';
# SELECT * FROM employees WHERE INITCAP(first_name) LIKE 'A%r%';

"""Character manipulations functions - функции которые манипулируют нашими тексами,символами"""
# CONCAT(s,s) примает 2 параметра объединяет строки, где s это строка.
# SELECT CONCAT(first_name,last_name) FROM employees;
# SELECT CONCAT('PRIvet ', 'Kak deLA?') FROM dual;
# SELECT CONCAT(salary*2, hire_date) FROM employees;
# SELECT SYSDATE FROM dual; ---> SYSDATE функция показывает сегоднешнию дату.
# SELECT CONCAT('Today Is ', SYSDATE) FROM dual;

# LENGTH(s) принимает 1 параметр вычисляет длинну строки где s это строка.
# SELECT first_name, LENGTH(first_name) AS len FROM employees;
# SELECT salary, LENGTH(salary) AS len_salary, hire_date, LENGTH(hire_date) AS len_date FROM employees;
# SELECT country_name FROM countries WHERE LENGTH(country_name) > 8;
# SELECT country_name FROM countries ORDER BY LENGTH(country_name);
