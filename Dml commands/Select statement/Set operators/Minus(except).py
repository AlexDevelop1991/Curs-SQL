"""MINUS 2-ух аутпут множеств возвращает только те строки которые есть в первом, но нет во втором,
удаляя при этом дубликаты и сортируя результат"""
# SELECT * FROM jobs WHERE job_id LIKE '%MAN%'
# MINUS
# SELECT * FROM jobs WHERE job_id LIKE '%MAN%'; ---> Ничего не будет

# SELECT * FROM jobs WHERE min_salary BETWEEN 4500 AND 8000
# MINUS
# SELECT * FROM jobs WHERE max_salary BETWEEN 10000 AND 15000;

