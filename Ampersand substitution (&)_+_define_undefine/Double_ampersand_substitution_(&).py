# SELECT first_name, last_name, salary
# FROM employees
# WHERE first_name LIKE '%&bukva%'
# AND last_name LIKE '%&bukva%'; ---> Не эффективный метод лучше так не писать.

# SELECT first_name, last_name, salary
# FROM employees
# WHERE first_name LIKE '%&&bukva%' --> Добавляем ещё один знак & и Oracle не будет два раза спрашивать.
# AND last_name LIKE '%&bukva%'; ---> В данном случаи ту букву которую вы введёте ORACLE запоминает эту букву на всю сессию и больше не будет вас просить ввести букву.

# SELECT first_name, last_name, &col FROM employees;

# SELECT first_name, last_name, &col FROM employees
# ORDER BY &col2;

# SELECT &select_list
# FROM &table_name
# WHERE &conditions
# ORDER BY &col2;

# UPDATE students SET &col3 = &value WHERE &conditions;

