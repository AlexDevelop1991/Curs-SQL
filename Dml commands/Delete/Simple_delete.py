"""DELETE"""
"""Удаляет одну или больше строк из таблицы"""

"""DELETE
FROM table_name
WHERE condition(s);"""

# DELETE FROM new_emps; Если не указывать WHERE удаляться все строки в таблице.

# DELETE FROM new_emps WHERE emp_id = 210;

# DELETE FROM new_emps WHERE job_id = 'ST_CLERK';

# DELETE FROM new_emps WHERE job_id LIKE '%CLERK%' OR name IS NULL;

