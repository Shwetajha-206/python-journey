# def test_local():
#     x = 10
#     print("Andar wala x:", x)

# test_local()
# print("Bahar wala x:", x)

# def test_local():
#     x = 10
#     print("Andar wala x:", x)

# test_local()

x = 10   # Yeh function ke BAHAR likha hai

# def test_global():
#     print("Andar wala x:", x)

# test_global()
# print("Bahar wala x:", x)
x = 10   # Global

# def change_x():
#     x = 20   # Yeh NAYA local x bana diya
#     print("Andar:", x)

# change_x()
# print("Bahar:", x)

# class Person:
#     def __init__(self,name,occ):
#         print("Hey I am a person")
#         self.name = name
#         self.occ = occ

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = Person("Harry","Developer")
# b = Person("Divya","HR")
# a.info()
# b.info()

# a.name = "Divya"
# a.occ = "HR"
# a.info()

# class Student:
#     #default Constructor
#     def __init__(self):
#         pass
#     college_name = "ABC college"
#     name = "anonymous"

    #parameterized constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         name = "Karan"
#         print("adding new student in Database..")

#     def welcome(self):
#         print("welcome student,",self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student("karan",97)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",88)
# print(s2.name,s2.marks)
# print(s2.college_name)
# print(s1.name)
# s1.welcome()
# s2 = Student()
# print(s1.name)
# print(s2.name)
# print(s1.get_marks())

#Question 2
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("hello")
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("hii",self.name, "your avg score is:",sum/3)
# s1 = Student("tony stark", [99,98,97])
# s1.get_avg()
# s1.name = "ironman"
# s1.get_avg()
# s1.hello()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = Car()
# car1.start()
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
