# Базовый синтаксис
```
SELECT перечень_полей (*) 
FROM имя_таблицы
WHERE условие
```

# Выборка всех полей по году выпуска
```
SELECT * 
FROM films
WHERE year = 2010
```

# Выборка названия по году выпуска
```
SELECT title 
FROM films
WHERE year = 2010
```
# Выборка названия и года в диапазоне по годам выпуска
```
SELECT title, year 
FROM films WHERE year > 2005 
AND year < 2010 AND duration < 90
ORDER BY year
```

#  То же самое, но с Between
```
SELECT title, year 
FROM films 
WHERE year BETWEEN 2005 AND 2010
ORDER BY year
```
# Пример не вполне корректного запроса
```
SELECT title
FROM films 
WHERE genre = 8
```
# Исправим (составной запрос)
```
SELECT title
FROM films 
WHERE genre = 8
```
# Выборка по перечню значений
```
SELECT title, duration FROM films 
WHERE duration IN (45, 60, 90)
ORDER BY duration DESC
```
# Выборка с группировкой по ID
```
SELECT * FROM films 
WHERE year >= 2001
AND duration BETWEEN 45 and 90
GROUP by id
```
# Выборка с LIKE
```
SELECT title FROM films 
WHERE title LIKE 'А_к%'
```
### Примечание:
- % - любое кол-во символов от 0 до INF
- _ - любой символ
- можно и NOT LIKE

# Выборка без повторов
```
SELECT DISTINCT year from films
ORDER by year
```
### Причечание:
- DISTINCT
# Выборка с объединением двух таблиц
```
SELECT
films.title as Фильм,
genres.title as Жанр
FROM films, genres 
WHERE films.genre = genres.id
```
# Выборка: сколько фильмов каких годов
```
SELECT year, count(*) as Кол_во
FROM films
GROUP BY year
ORDER BY Кол_во DESC
```
# Выборка: сколько фильмов каких годов, включая только те кол-ва, которые больше 500
```
SELECT year, count(*) as Кол_во
FROM films
GROUP BY year HAVING Кол_во > 500
ORDER BY Кол_во DESC
```
# Добавление записи в таблицу users
```
INSERT INTO 
users(name, age)
VALUES('Tom', 20),
('Tim', 41)
```

# Изменение возраста в записи users
```
UPDATE users
SET age=22
WHERE id=2
```

# Удалить в users тех, кто старше 30 лет 
```
DELETE from users
WHERE age > 30
```
