# Базы данных (запись)
"""
1. Импорт библиотеки sqlite3
2. Подключаемся к БД
3. Назначить "курсор"
4. Работаем с БД (запросы и ответы)
5. Подтвердить изменение (commit)
6. Отключаемся от БД
"""
import sqlite3
import csv

# Подключаемся
connection = sqlite3.connect('db/movies.sqlite')

# Курсор
cursor = connection.cursor()

# Запрос (с помощью курсора)
with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # пропустить заголовок (первая строка)
    for name, age in reader:
        cursor.execute(
            """
            INSERT INTO users(name, age)
            VALUES(?, ?)
            """, (name, int(age))
        )

connection.commit()  # Подтверждение
connection.close()  # Закрываем подключение
# fetchall - всё
# fetchone - только первое соответствие
# fetchmany(N) - N - соответствий
# array = result.fetchall()
#
# # print(array)
#
# for title, year in array:
#     print(title,  year)
