# Базы данных (чтение)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД (запросы и ответы)
5. Отключаемся от БД
"""
import sqlite3

# Подключаемся
connection = sqlite3.connect('db/movies.sqlite')

# Курсор
cursor = connection.cursor()

# Запрос (с помощью курсора)
result = cursor.execute(
    """
    SELECT title, year FROM films
    WHERE year BETWEEN 2001 AND 2005
    LIMIT 5
    """
)

# fetchall - всё
# fetchone - только первое соответствие
# fetchmany(N) - N - соответствий
array = result.fetchall()

# print(array)

for title, year in array:
    print(title,  year)