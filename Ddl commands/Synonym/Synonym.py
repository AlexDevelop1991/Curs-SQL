"""SYNONYM - это альтернативное имя объекта,обычно synonym даються на таблицы или view"""
"""SYNONYM бывают PRIVATE,PUBLIC"""

"""CREATE PUBLIC SYNONYM synonym_name
FOR object_name;"""

# CREATE SYNONYM syn5 FOR sudents;

# CREATE PUBLIC SYNONYM syn5 FOR sudents;

"""ALTER PUBLIC SYNONYM synonym_name COMPILE;"""

# ALTER SYNONYM syn5 COMPILE;

"""DROP  PUBLIC SYNONYM synonym_name;"""

# DROP PUBLIC SYNONYM syn5;