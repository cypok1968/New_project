# OOП Проектирование классов
from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Гаф"


class Cat(Animal):
    def make_sound(self):
        return "Мяу"


class Elephant(Animal):
    def make_sound(self):
        return "Протрубил"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def make_all_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())


dog = Dog()
cat = Cat()
elephant = Elephant()

zoo = Zoo()

zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(elephant)

zoo.make_all_sounds()



