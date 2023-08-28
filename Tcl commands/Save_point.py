"""SAVEPOINT savepoint_name;"""

# INSERT INTO new_emps VALUES (1000, 'Sasha', SYSDATE, 'IT_PROG');
# SAVEPOINT s1;
# UPDATE new_emps SET emp_id = 300 WHERE emp_id = 100;
# SAVEPOINT s2;
# DELETE FROM new_emps WHERE emp_id = 101;
# ROLLBACK TO SAVEPOINT s2;

