Name = "Shweta jha"
age = 20
height = 5.2

print("My Name is:",Name)
print("My Age is:", age)
print("My height is:", height)

x = 10
y = 10.5
z = "hello"
w = True
print(type(x))
print(type(y))
print(type(z))
print(type(w))

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
print(num1+num2)

a = int(input("Enter a nuumber:"))
b = int(input("Enter a number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

x = 7
y = 2
print(x/y)
print(x//y)

print(10>5)
print(10==10)
print(10!=5)

print(True and False)
print(True or False)
print(not True)

first_name = "Shweta"
last_name = "Jha"
full_name = first_name + " "+ last_name
print(full_name)

name = "Shweta jha"
print("First letter:",name[0])
print("last letter:", name[1])
print("Uppercase:", name.upper())

s ="programming"
print(s[2:6])

name = "Shweta"
print(len(name))

x = 25
x = int(x)
print((x)+5)

a = 10
print("Number is " + str(a))

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("Multiplication:",num1*num2)

x = float("3.14")
y = int(x)
print(y)

x = int(input("Enter a number:"))
if(x%2==0):
    print(x, "is even")
else:
    print(x, "is odd")

x = int(input("Enter a number:"))
if(x>0):
    print("Positive")
elif(x==0):
    print("Zero")
else:
    print("Negative")

x = int(input("Enter your age:"))
if(x >= 18):
    print("You can vote")
else:
    print("You cannot vote")

x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
z = int(input("Enter a number:"))

if(x>y and x>z):
    print("x is greater")
elif(y>x and y>z):
    print("y is greater")
else:
    print("z is greater")

x = int(input("Enter a number:"))
if (x%100 == 0):
    print("x is divisible")
else:
    print("X is not divisible")

i = 0
while(i<10):
    print(i)
    i = i+1

total = 0
num = int(input("Enter a number(0 to stop):"))

while(num != 0):
    total = total+num
    num = int(input("Enter a number: "))
print("Sum is:", total)

x = int(input("Enter a number:"))
fact = 1
i = 1

while(i<=x):
    fact = fact*i
    i = i + 1
print("Factorial is:", fact)

i = 10
while(i>0):
    print(i)
    i = i-1
print("Blast off!")

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if(num % i == 0):
            is_prime = False
            break
    if(is_prime):
        print(num)

for num in range(1,10):
    print(num)

for num in range(1,50):
    if(num % 2 == 0):
        print(num)

total = 0
for num in range(1,11):
    total = total+num
    print(total)

num = int(input("Enter a number:"))

for i in range(1,11):
    print(num, "*", i,"=", num*i)

name = input("Enter your name: ")

for letter in name:
    print(letter)

num = input("Enter a number:")
reversed_num = ""
for digit in num:
    reversed_num = digit+ reversed_num

if(num==reversed_num):
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")

rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end ="")
    print()

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is Greater")
    else:
        print("Second number is Greater")

a = 9
b = 8
calculateGmean(a,b)
isGreater(a,b)

def average(a,b):
    print("The average is:", (a+b)/2)
average(4,6)

def greet():
    print("welcome!")
greet()

def add(a,b):
    print("sum:",a+b)
add(5,3)

def square(n):
    return n*n
result = square(5)
print("square:", result)

def is_even(num):
   if (num%2 == 0):
      return True
   else:
      return False
num = int(input("Enter a number:"))
result = is_even(num)
print(result)

def find_max(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
result = find_max(3,4,5)
print(result)

def calculate_area(length,width):
    return length*width
result = calculate_area(5,4)
print(result)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

result = celsius_to_fahrenheit(9)
print(result)

def greet_person(name, greeting="Hello"):
    print(greeting, name)
greet_person("priya")
greet_person("Rahul","Hii")
greet_person("Shweta","Namaste")

def power(base, exponent=2):
    print(base**exponent)
power(2)
power(2)
power(2,3)


def factorial(n):
    fact = 1
    i = 1
    while(i <= n):
        fact = fact * i
        i = i + 1
    return fact

result = factorial(5)
print(result)

def sum_of_n(n):
    total = 0
    for i in range (1, n+1):
        total = total + i
    return(total)

result = sum_of_n(5)
print(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if (num % i == 0):
            return False
        return True
print(is_prime(7))
print(is_prime(8))
print(is_prime(1))

def print_table(num):
    for i in range(1,11):
     print(num , "*", i, "=", num*i)
print_table(5)

def check_grade(marks):
    if(marks>=90):
        return "A"
    elif(marks>=75):
        return "B"
    elif(marks>=60):
        return "C"
    else:
        return "Fail"
print(check_grade(95))
print(check_grade(80))
print(check_grade(65))
print(check_grade(40))

def count_vowels(word):
    count = 0
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            count = count+1
    return count
    
print(count_vowels("Priya"))
print(count_vowels("Programming"))

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("hello"))
print(reverse_string("Programming"))

def is_prime(num):
    if(num<2):
        return False
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)

print_primes_in_range(1, 50)