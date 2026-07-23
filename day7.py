#del keyword
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Shradhha")
del(s1)
print(s1)

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass())

#Inheritance

class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
print(car1.color)


class Book:
     def __init__(self,title,author,price):
          self.title = title
          self.author = author
          self.price = price

     def display(self):
         print("Title:", self.title)
         print("Author:", self.author)
         print("Price: Rs.", self.price)

book1 = Book("James","shweta",3456)
print(book1.title)    
print(book1.author)   
print(book1.price) 


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

area1 = Rectangle(3,4)
print(area1.area())


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print(f"Rs.{amount} deposited")

    def check_balance(self):
        print(f"Current balance: Rs.{self.__balance}")

account = BankAccount(5000)
account.deposit(1000)
account.check_balance()
print(account.__balance)

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    
calc = Calculator()

print(Calculator.add(10,5))
print(Calculator.subtract(10,8))
print(Calculator.multiply(9,5))

