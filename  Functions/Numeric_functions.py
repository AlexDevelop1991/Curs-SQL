                    ### Numeric Functions ###

"""ROUND(n,precision) округляет,принмает 2 параметра, 1 обязательный(n)."""
# n - это число.
# precision - точность.
# SELECT ROUND(7.4) FROM dual;
# SELECT ROUND(7.65769, 2) FROM dual;
# SELECT salary * 3.1415, ROUND(salary * 3.1415) FROM employees;
# SELECT ROUND(363576, -5) FROM dual;
# SELECT first_name, ROUND((SYSDATE - hire_date ) * employee_id) AS bonus FROM employees;

"""TRUNC(n,precision) обрезает(сокращает), принмает 2 параметра, 1 обязательный(n)."""
# SELECT TRUNC(7.657693, 4) FROM dual;
# SELECT TRUNC(36.3576, 1) FROM dual;
# SELECT first_name, ROUND((SYSDATE - hire_date ) * employee_id) AS bonus, TRUNC((SYSDATE - hire_date ) * employee_id)AS bonus2 FROM employees;

"""MOD(dividend,divisor) остаток от деления,принимает 2 параметра"""
# dividend - делимое.
# divisor - делитель.
# SELECT MOD(8, 3) FROM dual;
# SELECT MOD(8.5, 3.3) FROM dual;
# SELECT * FROM employees WHERE MOD(employee_id, 2) = 0;
# SELECT employee_id, first_name, last_name, MOD(employee_id, 3) + 1 AS team FROM employees;

