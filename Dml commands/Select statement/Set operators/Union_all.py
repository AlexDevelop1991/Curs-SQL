"""UNION ALL объединяет 2 аутпут множества в одно простым соединением."""
# SELECT * FROM jobs WHERE job_id LIKE '%MAN%'
# UNION ALL
# SELECT * FROM jobs WHERE job_id LIKE '%MAN%';

# SELECT job_id, job_title, min_salary FROM jobs WHERE job_id LIKE '%MAN%'
# UNION ALL
# SELECT job_id, job_title, min_salary FROM jobs WHERE job_id LIKE '%MAN%'
# ORDER BY min_salary;

# SELECT * FROM jobs WHERE job_id LIKE '%MAN%'
# UNION ALL
# SELECT * FROM jobs WHERE job_id LIKE '%MAN%'
# ORDER BY 3 DESC;

# SELECT first_name, last_name, salary FROM employees WHERE employee_id > 200
# UNION ALL
# SELECT job_id, job_title, max_salary FROM jobs WHERE job_id LIKE '%MAN%';

# 