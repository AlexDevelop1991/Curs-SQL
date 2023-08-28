"""AVG({DISTINCT | ALL} expression) Игнорирует NULL"""

# SELECT AVG(salary) FROM employees;
# SELECT AVG(salary) FROM employees WHERE job_id = 'IT_PROG';
# SELECT ROUND(AVG(salary)), ROUND(AVG(DISTINCT salary)) FROM employees;
# SELECT COUNT(*) a, SUM(salary) b, AVG(commission_pct) c FROM employees;
# SELECT ROUND(AVG(SYSDATE - hire_date) / 365) FROM employees;
# SELECT AVG(NVL(commission_pct, 0)) FROM employees;
