                    ### Character Function ###
"""Case conversion functions - функции которые работаюм с регистром букв."""

"""LOWER(s) принимает 1 параметр где (s) это строка,текст (выводить текст,строку маленькими буквами)."""
# SELECT first_name, LOWER(first_name) FROM employees;
# SELECT * FROM employees WHERE LOWER(first_name) = 'david';
# SELECT * FROM employees WHERE LOWER(first_name) LIKE '%en%';
# SELECT LOWER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;

"""UPPER(s) примает 1 параметр где (s) это строка,текст (выводит текст,строку большими буквами)."""
# SELECT first_name, UPPER(first_name) FROM employees;
# SELECT * FROM employees WHERE UPPER(first_name) LIKE '%EN%';
# SELECT UPPER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;

"""INITCAP(s) принимает 1 параметр где (s) это строка,текст (В каждос слове делает первую букву заглавной(большой) а остальные маленькие."""
# SELECT INITCAP('PRIVET kak dElA?888') FROM dual;
# SELECT INITCAP('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;
# SELECT * FROM employees WHERE INITCAP(first_name) = 'David';
# SELECT * FROM employees WHERE INITCAP(first_name) LIKE 'A%r%';

"""Character manipulations functions - функции которые манипулируют нашими тексами,символами"""

"""CONCAT(s,s) примает 2 параметра объединяет строки, где s это строка."""
# SELECT CONCAT(first_name,last_name) FROM employees;
# SELECT CONCAT('PRIvet ', 'Kak deLA?') FROM dual;
# SELECT CONCAT(salary*2, hire_date) FROM employees;
# SELECT SYSDATE FROM dual; ---> SYSDATE функция показывает сегоднешнию дату.
# SELECT CONCAT('Today Is ', SYSDATE) FROM dual;

"""LENGTH(s) принимает 1 параметр вычисляет длинну строки где s это строка."""
# SELECT first_name, LENGTH(first_name) AS len FROM employees;
# SELECT salary, LENGTH(salary) AS len_salary, hire_date, LENGTH(hire_date) AS len_date FROM employees;
# SELECT country_name FROM countries WHERE LENGTH(country_name) > 8;
# SELECT country_name FROM countries ORDER BY LENGTH(country_name);

"""LPAD(s,n,p) - добавление определённых символов влево от нашей строки,где s это строка, n конечная длинна текста, p текст для заполнения.
   RPAD(s,n,p) -  добавление определённых символов вправо от нашей строки,где s это строка, n конечная длинна текста, p текст для заполнения."""
# SELECT LPAD('Alex', 7, '$') FROM dual;
# SELECT RPAD('Alex', 7, '$') FROM dual;
# SELECT first_name, LPAD(first_name, 25, '#') FROM employees;
# SELECT first_name, LPAD(first_name, 25, '#'), RPAD(first_name, 25, '#') FROM employees;
# SELECT RPAD(first_name, 15, ' ') || LPAD(salary, 8, ' ') FROM employees;

"""TRIM({trailing | leading | both}trimstring from s) удаляет символ( сначала или с конца или и сначала и с конца нашего текста)."""
# trailing ---> удалит с конца текста.
# leading ---> удалит с начало тескта.
# both ---> удалит и с начала и с конца текста.
# trimstring - текст который надо срезать FROM s - откуда срезать.
# SELECT TRIM(TRAILING 'q' FROM 'Alexqqqqq') FROM dual;
# SELECT TRIM(LEADING '#' FROM '#####Alex##') FROM dual;
# SELECT TRIM(BOTH '#' FROM '#####Alex###') FROM dual;
# SELECT TRIM('   Alex  Brovco   ') FROM dual;
# SELECT TRIM(BOTH 7 FROM 755477) FROM dual;

"""INSTR(s, search string, start position, Nth occurrence) принимает 4 параметра 2  обязательны(s, search string)."""
# INSTR - возвращает позицию искомого текста в нашем тексте.
# s - это строка.
# search string - искомый текст.
# start position - позиция для начало работы.
# Nth occurrence - N-ое появление.
# SELECT * FROM employees WHERE INSTR(job_id, 'PROG') = 4;
# SELECT INSTR('Alex Brovco', 'B') FROM dual;
# SELECT INSTR('Alex Brovco', 'o', 2, 2) FROM dual;

"""SUBSTR(s, start position, number of characters) принимает 3 параметра 2 обязательны(s, start position)"""
# s - строка
# start position - позиция для начало работы.
# number of characters - количество символов.
# SELECT email, SUBSTR(email, 4) FROM employees;
# SELECT email, SUBSTR(email, 6, 2) FROM employees;
# SELECT salary, SUBSTR(salary, 2, 3) FROM employees;
# SELECT SUBSTR('Privet, kak dela??', 7) FROM dual;
# SELECT SUBSTR('Privet, kak dela??', -4) FROM dual;

"""REPLACE(s, search item, replacement item) принимает 3 параметра 2 обязательных(s,search item) что то меняет на что то."""
# s - строка
# search item - искомый элемент
# replacement item - заменяющий элемент
# SELECT REPLACE('Privet, kak dela? Vse horoso!', 'e', '*') FROM dual;
# SELECT REPLACE('Privet, kak dela? Vse horoso!', 'e', 'aaaa') FROM dual;
# SELECT REPLACE('Privet, kak dela? Vse horoso!', 'a') FROM dual;
# SELECT salary, REPLACE(salary, '1', '9') FROM employees;
# SELECT hire_date, REPLACE(hire_date, '.', '/') FROM employees;