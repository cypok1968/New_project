# CSV-файлы
import csv

data = [
    ['name', 'age', 'city'],
    ['Борис', '25', 'Воронеж'],
    ['Владимир', '28', 'Тверь'],
    ['Глеб', '35', 'Москва']
]

with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
