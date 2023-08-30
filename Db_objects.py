                   ### DB OBJECTS ###
"""1.TABLE - таблица"""

"""2.VIEW - вид """

"""3.SUNOSYM - Синоминим это альяс для таблицы или для View"""

"""4.INDEX - Индекс служит для увеличение производительности поиска какой либо информации."""

"""5.SUQUENCE - Последовательность,генирирует уникальные значения """

# select object_type , count(object_type) from user_objects
# group by object_type order by object_type;

# select object_type , count(object_type) from all_objects
# group by object_type order by object_type;