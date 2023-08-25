# INSERT INTO employees (employee_id, last_name, email, hire_date, job_id)
# VALUES (210, 'Brovco', 'ABROVCO', '25-AUG-2023', 'IT_PROG'); ---> Так лучше не писать

# INSERT INTO employees (employee_id, last_name, email, hire_date, job_id)
# VALUES (211, INITCAP('sirghi'), UPPER('msirghi'), TO_DATE('20-AUG-2023', 'DD-MON-YYYY'), UPPER('it_prog')); ТАК ЛУЧШЕ.

# INSERT INTO employees (employee_id, last_name, email, hire_date, job_id)
# VALUES (200 + 12, INITCAP('popa'), UPPER('popa23'), SYSDATE, UPPER('it_prog'));

# 