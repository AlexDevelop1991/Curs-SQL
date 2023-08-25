"""UPDATE"""
"""Меняет информацию в уже существуещих строках которые были добавлены  с помощью INSERT
или какими то другими средствами.Может изменять информацию для одной строки или для нескольких строк
так же может менять информацию в одном столбце или  в нескольских столбцах одной или нескольких строк
НЕ МОЖЕТ  менять информацию в нескольких таблицах всегда работает только с ОДНОЙ таблицой"""

"""UPDATE table_name
        SET
column(s) = value(s)
WHERE condition(s);"""

# UPDATE employees SET salary = 10000 WHERE employee_id = 100;

# UPDATE employees SET salary = salary * 2 WHERE employee_id = 100;

# UPDATE employees SET salary = 27000, job_id = 'IT_PROG' WHERE employee_id = 101;

# UPDATE employees SET salary = 8000 WHERE employee_id < 105;

# UPDATE employees SET salary = 100; Если не указывать WHERE,то информация поменяеться во всех строках.

