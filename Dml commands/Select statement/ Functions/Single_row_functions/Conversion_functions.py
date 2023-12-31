                    ### Conversion Functions ###
         # TO_CHAR           # TO_DATE           # TO_NUMBER

"""TO_CHAR(number to char) возвращает нам тип VARCHAR2 """
"""TO_CHAR(number, format mask, nls_parameters) = T(text) """
# Конвертация числа в текст,используя функцию TO_CHAR означет взять число и сделать из него текст в том виде,в каком указан наш формат,если таковой имеется.

# Элемент     # Описание                            # Формат               # Число      # Текст
#   9           Ширина                                99999                  18           18
#   0           Отображение нуля                      099999                 18           000018
#   .           Позиция десятичной точки              099999.999             18.35        000018.350
#   D           Позиция десятичного разделителя       099999D999             18.35        000018.350
#   ,           Позиция запятой                       099,999,999            1234567      001,234,567
#   G           Позиция разделителя групп             099999G999             1234567      001,234,567
#   $           Знак $                                $099999                18           $000018
#   L           Локальная валюта                      L099999                18           $000018
#   MI          Позиция знака -                       099999MI               -18          000018-
#   PR          Скобки для отрицательных чисел        099999PR               18           <000018>
#   S           Префикс + или -                       S099999                18           +000018


"""TO_CHAR(date to char) возвращает нам тип VARCHAR2 """
"""TO_CHAR(data, format mask, nls_parameters) = T(text) """
#  Конвертация даты в текст,используя функцию TO_CHAR означет взять дату и сделать из неё текст в том виде,в каком указан наш формат,если таковой имеется.
# SELECT hire_date, TO_CHAR(hire_date, 'Month', 'NLS_DATE_LANGUAGE = RUSSIAN') FROM employees;
# SELECT hire_date, TO_CHAR(hire_date, 'fmMonth') || 'hello!' FROM employees; ---> fm убирает лишнии пробелы с имён,дней и месяцев.
# SELECT first_name, hire_date FROM employees WHERE TO_CHAR(hire_date, 'fmMonth')= 'August';

                    # ДАТА для Примера: '20-SEP-19'
# Элемент        # Описание                                     # Текст
# Y                Последняя цифра года                           9
# YY               Последнии 2 цифры года                         19
# YYY              Последнии 3 цифры года                         019
# YYYY             Год целиком                                    2019
# RR               Год в формате 2-х цифр                         19
# YEAR             Буквенное написание года(Case-sensitive)       TWENTY NINETEEN
# MM               Месяц в формате 2-х цифр                       09
# MON              3 буквы из названия месяца(Case-sensitive)     SEP
# MONTH            Буквенное написание месяца(Case-sensitive)     SEPTEMBER

# D                День недели                                    6
# DD               День месяца 2 цифры                            20
# DDD              День года                                      263
# DY            3 буквы из названия дня недели(Case-sensitive)    FRI
# DAY              Полное название дня недели(Case-sensitive)     FRIDAY
# W                Неделя месяца                                  3
# WW               Неделя года                                    38
# Q                Квартал года                                   3
# CC               Век                                            21

                    # ДАТА для Примера: '20-SEP-19 16:17:18'
# AM PM,A.M и P.M  Индикатор                                      PM
# HH,HH12 и HH24   Формат времени                                 04,04,16
# MI               Минуты                                         17
# SS               Секунды                                        18
# SSSSS            Секунды после полуночи                         58638
# -/.,?#!          Пунктуация:'MM.YY'                             09.19
# 'Любой текст'    '"Quarter" Q "of" Year'                         Quarter 3 of Twenty Nineteen
# TH               'DDth "of" Month'                              20th of September
# SP               Буквенное написание(spell)'MmSP Month Yyyysp'  Nine September Two Thousand Nineteen
# THSP или SPTH    Комбинация:'hh24SpTh'                          sixteenth

"""TO_DATE(char to date)"""
"""TO_DATE(text, format mask, nls_parameters) = D(data)"""
# Конвертация текста в дату,используя функцию TO_DATE означает взять текст и объяснить в своём формате,где и как содержится информация о элементах даты в вашем тексте.
# SELECT TO_DATE('18:40 2019!17-Sep', 'HH24:MI YYYY!DD-Mon') FROM dual;
# SELECT TO_CHAR(TO_DATE('28-Sep-19 15:16:17', 'DD-Mon-RR HH24:MI:SS'), 'DD-Mon-RR HH24:MI:SS') FROM dual;
# SELECT * FROM employees WHERE hire_date > TO_DATE('01-Jan-05', 'DD-Mon-RR');
# SELECT TO_CHAR(TO_DATE('15?1987$17$18$19/09', 'hh24?YYYY$MI$SS$DD/mm'), 'dd-MON-yyyy hh24:mi:ss') as new_date FROM dual;

"""TO_NUMBER(number to date)"""
"""TO_NUMBER(text, format mask, nls_parameters) = N(number)"""
# Конвертация текста в число,используя функцию TO_NUMBER означает взять текст и объяснить в своём формате,где и как содержится информация о элементах числа в вашем тексте.
# SELECT TO_NUMBER('$4538.56', '$999999.999') FROM dual;
# SELECT TO_NUMBER('<4832.34>', '99999.999PR') FROM dual;
# SELECT TO_NUMBER('3.17', '99.9') FROM dual; Будет ошибка так как текст нельзя округлить.
# SELECT TO_CHAR(3.17, '99.9') FROM dual; Здесь всё нормально так как число можно округлить.


"""Nested(вложенные) single-row функции"""
# SELECT TO_DATE('18-09-87', 'DD-MM-RR'), TO_CHAR(TO_DATE('18-09-87', 'DD-MM-RR'), 'Day'),LENGTH( TO_CHAR(TO_DATE('18-09-87', 'DD-MM-RR'), 'fmDay')) FROM dual;
# SELECT first_name, NVL(SUBSTR(first_name, 6), 'Name is too short') FROM employees;
# SELECT first_name, commission_pct, NVL(salary * commission_pct, 500) AS bonus FROM employees;


