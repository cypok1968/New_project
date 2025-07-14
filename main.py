# JSON - (Java Script Object Notation)
# Для чтения:
# load() - читает из файла
# loads() - читает строковое представление
import json

d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 120,
    'груша': 280,
}

# запись напрямую в файл
# with open('fruits.json', 'w', encoding='utf-8') as f:
#     json.dump(d, f, indent=4)

# вывод в виде строки
data = json.dumps(d, indent=4)
print(data)

# with open('dogs.json', 'rt') as d:
#     # data = json.load(d) # Напрямую из файла
#     temp = d.read()  # читаем файл как строку
#     data = json.loads(temp)  # строковое представление JSON
#
# for i in range(len(data)):
#     print(f'Питомец №{i + 1}:')
#     for k, v in data[i].items():
#         if type(v) == list:
#             print(f'\t{k}: {', '.join(v)}')
#         else:
#             print(f'\t{k}: {v}')

# for k, v in data.items():
#     if type(v) == list:
#         print(f'{k}: {', '.join(v)}')
#     else:
#         print(f'{k}: {v}')

# Zip
# from zipfile import ZipFile
# import os

# csv_files = [f for f in os.listdir() if f.endswith('.csv')]
# # print(csv_files)
# with ZipFile('archive.zip', 'w') as myzip:
#     for file in csv_files:
#         myzip.write(file)
#         os.remove(file)
# files_to_extract = ['people.csv', 'file.csv']
#
# # Распаковать
# # with ZipFile('archive.zip', 'r') as zip_obj:
# #     zip_obj.extractall(members=files_to_extract)
#
# # Получить список
# with ZipFile('archive.zip', 'r') as zip_obj:
#     print(zip_obj.namelist())


# CSV-файлы (strptime)
# import csv

# with open('people.csv', 'r', encoding='utf-8') as f:
#     dict_reader = csv.DictReader(f)
#     for row in dict_reader:
#         print(f'{row['name']} живёт в городе {row['city']}')

# field_names = ['name','age','city']
# data = {
#     'name' : 'Борис',
#     'age': 27,
#     'city': 'Москва'
# }
#
# with open('file.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=field_names)
#     writer.writerow(data)

# Режимы квотирования
# data = ['name', 25, 'town']
# with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)

# data = [
#     ['name', 'age', 'city'],
#     ['Борис', '25', 'Воронеж'],
#     ['Владимир', '28', 'Тверь'],
#     ['Глеб', '35', 'Москва']
# ]
#
# with open('people.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         print(row)
#
# with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
