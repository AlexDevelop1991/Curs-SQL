                    ### Date Functions ###

# SELECT * FROM nls_session_parameters WHERE parameter = 'NLS_DATE_FORMAT'; ---> так проверяеться формат даты.
# SELECT TO_CHAR(SYSDATE, 'DD-MM-RR hh24:mm:ss') FROM dual; ---> так можно получить время.
# SELECT * FROM sys.nls_session_parameters; ---> выводит служебную таблицу.

"""SYSDATE - возвращает время нашего DATA BASE сервера то есть база данных которая на сервере"""
# SELECT SYSDATE FROM dual;
# SELECT SYSDATE - hire_date FROM employees; --> когда дату отнимаешь от даты получаешь количества дней.

"""MONTHS_BETWEEN(start_date, end_date) ищёт количества месяцев между определенными датами."""
# start_date - дата с.
# end_data - дата по.
# SELECT employee_id, MONTHS_BETWEEN(end_date, start_date) FROM job_history;
# SELECT MONTHS_BETWEEN('12.02.19', '05.01.19') FROM dual;
# SELECT MONTHS_BETWEEN('12.05.19', '11.05.19') * 31 FROM dual;

"""ADD_MONTHS(date, number_of_months) добавляет месяц."""
# date - дата.
# number of months - количество месяцев.
# SELECT end_date, ADD_MONTHS(end_date, 4) FROM job_history;
# SELECT end_date, ADD_MONTHS(end_date, -4) FROM job_history;
# SELECT ADD_MONTHS('30.09.19' , 1) FROM dual;
# SELECT ADD_MONTHS('31.12.19' , 2) FROM dual;

"""NEXT_DAY(date, day_of_the_week) следущий день"""
# date - дата.
# day of the week - день недели.
# SELECT NEXT_DAY(SYSDATE, 1) FROM dual; У америкосов 1 это воскресенье а у русских понедельник.
# SELECT NEXT_DAY('31.12.19', 'Пнд') - 7 FROM dual;

"""LAST_DAY(date) функция показывает последний день месяца."""
# SELECT LAST_DAY(SYSDATE) FROM dual;
# SELECT LAST_DAY('01.03.15') FROM dual;
# SELECT hire_date, LAST_DAY(hire_date) - hire_date AS prorabotal FROM employees;

"""ROUND(date, date precision format) округляет,принимает 2 параметра 1 обязательный(date)."""
# По default округляет до дня.
# date - дата.
# date precision format - точность округления.(Век-СС; Год-YYYY; Четверть-Q; Месяц-MM; Неделя-W; День-DD; Час-HH; Минута-MI.
# SELECT hire_date, LAST_DAY(hire_date) - hire_date AS prorabotal FROM employees;

"""TRUNC(date, date precision format) обрезает(сокращает),принимает 2 параметра 1 обязательный(date)."""
# По default округляет до дня.
# date - дата.
# date precision format - точность обрезает(сокращает).
# SELECT hire_date, TRUNC(hire_date, 'YYYY') FROM employees WHERE employee_id IN (120, 121);
