                    ### Date Functions ###
# SELECT * FROM nls_session_parameters WHERE parameter = 'NLS_DATE_FORMAT'; ---> так проверяеться формат даты.
# SELECT TO_CHAR(SYSDATE, 'DD-MM-RR hh24:mm:ss') FROM dual; ---> так можно получить время.

# SYSDATE - возвращает время нашего DATA BASE сервера то есть база данных которая на сервере
# SELECT SYSDATE FROM dual;
# SELECT SYSDATE - hire_date FROM employees; --> когда дату отнимаешь от даты получаешь количества дней.

# MONTHS_BETWEEN(start_date, end_date) ищёт количества месяцев между определенными датами.
# start_date - дата с.
# end_data - дата по.
# SELECT employee_id, MONTHS_BETWEEN(end_date, start_date) FROM job_history;
# SELECT MONTHS_BETWEEN('12.02.19', '05.01.19') FROM dual;
# SELECT MONTHS_BETWEEN('12.05.19', '11.05.19') * 31 FROM dual;

