                    ### Character Function ###
"""Case conversion functions - функции которые работаюм с регистром букв."""\
# Lower(s) принимает 1 параметр где (s) это строка,текст (выводить текст,строку маленькими буквами)
# SELECT first_name, LOWER(first_name) FROM employees;
# SELECT * FROM employees WHERE LOWER(first_name) = 'david';
# SELECT * FROM employees WHERE LOWER(first_name) LIKE '%en%';
# SELECT LOWER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;

# Upper(s) примает 1 параметр где (s) это строка,текст (выводит текст,строку большими буквами)
# SELECT first_name, UPPER(first_name) FROM employees;
# SELECT * FROM employees WHERE UPPER(first_name) LIKE '%EN%';
# SELECT UPPER('Privet ' || 'SkoLIKO tebe LET? ' || 'Mne 32') FROM dual;