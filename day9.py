#Property

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"

# stu1 = Student(98,97,96)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)

#Polymorphism and use of dunder function and __init__ function is also a dunder function
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNum(self):
#         print(self.real,"i+",self.img,"j")

#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex (newReal,newimg)

#     def __sub__(self,num2):
#             newReal = self.real - num2.real
#             newimg = self.img - num2.img
#             return Complex (newReal,newimg)


# num1 = Complex(1,3)
# num1.showNum()

# num2 = Complex(4,6)
# num2.showNum()

# num3 = num1 - num2
# num3.showNum()


#Prcatice Question
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius ** 2

#     def perimeter(self):
#         return 2 * (22/7) *self.radius 

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())


# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role:", self.role)
#         print("dept:", self.dept)
#         print("salary:", self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer" , "IT" , "80000")

# eng1 = Engineer("Elon Musk" , 40)
# eng1.showDetails()


# e1 = Employee("accountant" , "Finance" , "60000")
# e1.showDetails()


# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self,odr2):
#         return self.price > odr2.price

# odr1 = Order("chips", 20)
# odr2 = Or  der("Tea", 15)

# print(odr1>odr2)


#Decorator

#Step 1 — "Wrapper"

# def cook_food():
#     print("Khana bana diya")

# def wrapper():
#     print("Haath dho lo")
#     cook_food()
#     print("Table saaf kro")

# wrapper()

def my_decorator(func):
    def wrapper():
        print("Haath dho lo")
        func()
        print("Table saaf kro")
    return wrapper

@my_decorator
def cook_food():
    print("Khana bna diya")

cook_food()



