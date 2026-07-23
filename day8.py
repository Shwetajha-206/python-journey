class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog1 = Dog()
dog1.make_sound()   
dog1.bark()

class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def give_raise(self,amount):
        self.__salary+=amount

emp1 = Employee("Rahul",30000)
print(emp1.get_salary())

emp1.give_raise(5000)
print(emp1.get_salary())

class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class bike(Vehicle):
    pass
class car(Vehicle):
    pass

bike1 = bike()
car1 = car()

print("----Bike----")
bike1.start()
bike1.stop()

print("----Car----")
car1.start()
car1.stop()

#Multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type 

car1 = Fortuner("diesel")
car1.start()

#Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

#super Keyword
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started")

    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Pirius","electric")
print(car1.type)

#class Method

class Person:
    name ="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person
p1.changeName("rahul Kumar")
print(p1.name)
print(Person.name)