                        ### Некоторые термины ###

"""1. База данных - совокупность данных, которые хранятся по определённым правилам
и используються для удовлетворения информационных потребностей пользователей"""

"""2. Реляционная БД - это БД, где вся информация представляеться в виде таблиц"""

                    ### Знакомство с HR схемой ###

"""3. User - это лицо которое может подключиться к БД (log on process)"""

"""DB схема - это все объекты в БД, которые принадлежат одному user-у"""

                    ### SQL Команды ###

"""DML(Data Manipulation Language) команды - это те команды которые работают с внутриностью таблицы, напрямую с данными в таблице"""
# SELECT(выбрать) - делает выборку из таблиц то есть он находит в наших таблицах то что нам нужно.
# INSERT(вставлять) - с помощью этой команды можно вставлять строки в нашу таблицу,добавлять новый строки.
# UPDATE(изменять) - с помощью этой команды мы можем изменять данные в нашей таблице.
# DELETE(удалять) -  с помощью этой команды мы можем удвлить строку или строки из нашей таблицы.
# MERGE(объединять) - может объединить функциональность INSERT,UPDATE,DELETE

"""DDL(Data Definition Language) команды - напрямую с данными в таблице и других объектов  они не работают,они работают с самой таблицой в целом
или не с самой таблицой а со структурой этой таблице."""
# CREATE(создать) - с помощью этой команды мы можем создавать таблицы.
# ALTER(изменять) - с помощью этой команды можем изменять структуру таблицы например в таблице можем добавить новый столбец.
# DROP(удалять) - удаляет наши объекты из таблицы.
# RENAME(поменять) - можем поменять названия столбца в нашей таблицы.
# TRUNCATE - удаляет все данные из нашей таблицы,то есть таблица остаёться а всё что было в ней удаляется.

"""TCL(Transaction Control Language) команды - контроль транзакций"""
# COMMIT - это подтвердить
# ROLLBACK - это откатить
# SAVEPOINT - это точка сохранения

"""DCL(Data Control Language) команды"""
# GRANT - даёте какие то права
# REVOKE - отбираете какие то права
