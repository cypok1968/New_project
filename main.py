# OOП Class
"""
Задача: создать классы для моделирования клиентов банка и их счетов.
Условия:
	Класс BankAccount с атрибутами: _owner_name, balance.
	Методы: deposit(amount), withdraw(amount), get_balance().

"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Депозит пополнен на сумму {amount}.')
        else:
            print(f'Нельзя вносить отрицательную сумму на депозит.')

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f'С депозита снята сумма {amount}.')
        else:
            print(f'Не хватает средств. Овердрафт не доступен.')


client1 = BankAccount('John')
client1.deposit(500)
client1.withdraw(600)
print('Остаток:', client1.get_balance())

# OOП (inheritance)
# класс, от которого наследуем: базовый, родительский, суперкласс
# класс, который наследуется: производный, дочерний
# from math import pi
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def info(self):
#         print(f'Класс: {self.__class__.__name__}')
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# # Фигуры
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         self.name = 'круг'
#
#     def perimetr(self):
#         return round(2 * pi * self.radius, 2)
#
#     def area(self):
#         return round(pi * self.radius ** 2, 2)
#
#     def get_name(self):
#         return self.name
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.name = 'прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def get_name(self):
#         return self.name
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.name = 'квадрат'
#
#
# class Triangle(Square):
#     def __init__(self, side):
#         super().__init__(side)
#         self.side = side
#         self.name = 'треугольник'
#
#     def area(self):
#         return (self.side ** 2 * 3 ** 0.5) / 4
#
#     def perimetr(self):
#         return self.side * 3
#
#
# s = Square(5)
# print(s.area())
# print(s.perimetr())
# print(s.get_name())
# s.info()
#
# circle = Circle(5)
# print(circle.area())
# print(circle.perimetr())
# print(circle.get_name())
# circle.info()
#
# tr = Triangle(8)
# print(tr.area())
# print(tr.perimetr())
# print(tr.get_name())
# tr.info()

# method override; operator overloading
# __call__ - экземпляр класса становится вызываемым
# (как функция)
# y = ax^2 + bx + c
# class SquareFunction:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * x ** 2 + self.b * x + self.c
#
#
# s = SquareFunction(1, 2, 3)
# print(s(2))

# class MyTime:
#     def __init__(self, minutes, seconds):
#         if 0 <= minutes < 60:
#             self.minutes = minutes
#         if 0 <= seconds < 60:
#             self.seconds = seconds
#
#     def __add__(self, other):
#         m = self.minutes + other.minutes
#         s = self.seconds + other.seconds
#         m += s // 60
#         s = s % 60
#         m = m % 60
#         return MyTime(m, s)
#
#     def __str__(self):
#         return f'<Time {self.minutes:02}:{self.seconds:02}>'
#
#
# t1 = MyTime(13, 0)
# t2 = MyTime(53, 5)
# print(t1 + t2)

# from math import hypot
#
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'<Point: ({self.x}, {self.y})>'
#
#     def __repr__(self):
#         return f'<List of Points: ({self.x}, {self.y})>'
#
#     def __sub__(self, other):
#         return Point(abs(self.x - other.x), abs(self.y - other.y))
#
#     def __add__(self, other):
#         return hypot(self.x - other.x, self.y - other.y)
#
#
# p1 = Point(5, 4)
# p2 = Point(10, 2)
# print(p1 - p2)
# print(p1 + p2)
# str(a) -> a.__str__()
# isinstance(объект, тип) -> True
# isinstance(объект, (тип1,  тип 2, тип N)) -> True

# lst = list(range(1, 15))
# lst += ['a']
#
# class Stat:
#     def __init__(self, vals):
#         self.values = vals[:]  # получаем копию
#
#     def is_all_int(self) -> bool:
#         return all(isinstance(item, int) for item in self.values)
#
#     def get_min(self):
#         if self.is_all_int():
#             return min(self.values)
#         return None
#
#     def get_max(self):
#         if self.is_all_int():
#             return max(self.values)
#         return None
#
#     def get_aver(self):
#         if self.is_all_int():
#             return sum(self.values) / len(self.values)
#         return None
#
#
# s = Stat(lst)
# print(s.get_min())
# print(s.get_max())
# print(s.get_aver())

# class Selector:
#     def __init__(self, vals):
#         self.values = vals[:]  # получаем копию
#
#     def get_odd(self):
#         return [x for x in self.values if x % 2 == 1]
#
#     def get_even(self):
#         return [x for x in self.values if x % 2 == 0]
#
#
# s = Selector(lst)
# print(s.get_odd())
# print(s.get_even())
# print(lst)

# from lib import Student, Employee, Person
#
# people = [
#     Person('Александр', 27),
#     Student('Дмитрий', 'ГУАП'),
#     Employee('Пётр', 'Авангард'),
# ]
#
# for person in people:
#     if isinstance(person, Student):
#         print(person.get_univercity())
#     elif isinstance(person, Employee):
#         print(person.get_company())
#     else:
#         print(person.get_name())

# from lib import Circle, Rectangle, Square
#
# # def shape_info(shape: object):
# #     print(f'Площадь {shape.get_name()}а: {shape.area()}, Периметр: {shape.perimetr()}')
# rect, c, sqr = 'прямоугольник', 'круг', 'квадрат'
#
#
# def shape_info(shape: object):
#     if isinstance(shape, Circle):
#         fig = c
#     elif isinstance(shape, Rectangle):
#         fig = rect
#     elif isinstance(shape, Square):
#         fig = sqr
#     print(f'Площадь {fig}а: {shape.area()}, Периметр: {shape.perimetr()}')
#
#
# s = Square(10)
# shape_info(s)
#
# cr = Circle(10)
# shape_info(cr)
#
# r = Rectangle(5, 2)
# shape_info(r)

# print(dir(s))
# print(dir(cr))

# from lib import Book
#
# book = Book('Язык С++', 'Бьярн Страупструп')
#
# print(f'{book.get_title(), book.get_author()}')

# print(1 + 2)
# print(1 + 2.0)
# print('abc' + 'def')
# print([1, 2] + [3, 4])
#
# def func(x, y):
#     return x + y
#
# print(func(2, 3.0))
