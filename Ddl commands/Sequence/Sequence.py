"""CREATE SEQUENCE schema.sequence_name
INCREMENT BY number
START WITH number
{MAXVALUE number | NOMAXVALUE}
{MINVALUE number | NOMINVALUE}
{CYCLE | NOCYCLE}
{CACHE number | NOCACHE};"""

"""INCREMENT BY - увеличь на (число).
START WITH - с какого числа начинаем.
MAXVALUE - максимальное значения,по default(NOMAXVALUE).
MINVALUE - минимальное значения,по default (NOMINVALUE).
CYCLE - цикл,по default(NOCYCLE).
CACHE - кэш,по default (20).
nextval - следущие значеия.
currval - нынешнее значения."""

# CREATE SEQUENCE s1;

# SELECT s1.nextval FROM dual; ---> SEQUENCE выдаёт следущее значения.Уникально для всех значений все зависимости от сессии.
# SELECT s1.currval FROM dual; ---> SEQUENCE выдаёт значения в данный момент.В текущей сессии.

# CREATE SEQUENCE seq_faculty START WITH 20 INCREMENT BY 5;

# INSERT INTO faculties VALUES (seq_faculty.nextval, 'IT'); ---> Так делаем INSERT в таблицу.
# INSERT INTO students VALUES (seq_st.nextval, 'Alex', 3, seq_faculty.currval);

# CREATE SEQUENCE s3 INCREMENT BY 2 MAXVALUE 17;

# CREATE SEQUENCE s4 INCREMENT BY 2 MAXVALUE 17 CYCLE CACHE 3;


"""ALTER SEQUENCE schema.sequence_name
INCREMENT BY number
{MAXVALUE number | NOMAXVALUE}
{MINVALUE number | NOMINVALUE}
{CYCLE | NOCYCLE}
{CACHE number | NOCACHE};"""

# ALTER SEQUENCE seq_st INCREMENT BY 5;

"""DROP SEQUENCE schema.sequence_name;"""

# DROP SEQUENCE seq_st;

