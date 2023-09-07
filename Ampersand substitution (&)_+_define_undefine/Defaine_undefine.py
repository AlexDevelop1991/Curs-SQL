# SELECT first_name, last_name, salary
# FROM employees
# WHERE first_name LIKE '%&&bukva%'
# AND last_name LIKE '%&bukva%';
# UNDEFINE bukva; ---> Так мы можем вручную сбросить букву которую ввели в переменную bukva.

"""DEFINE"""

# DEFINE; --> С помощью DEFINE мы можем определить для конкретной переменной конкретное значение

# DEFINE bukva = e; --> При помощи этого statement мы задали новое знаечние для переменной bukva.

"""Команда SET DEFINE OFF с помощью этой команды мы можем сделать так чтобы ORACLE не воспринимал AMPERSAND 
как призыв запросить у вас значения. Если хотите вернуть функциональность AMPERSAND вы должны написать SET DEFINE ON"""