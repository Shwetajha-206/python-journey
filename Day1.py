#First python program

input("What's your name? ")
print("hello, world")

#Variables
name = input("What's your name? ")
print("hello,")
print(name)

#Improving my First python program
name = input("What's your name? ")
print("hello,",name)

#Strings and parameters
name = input("What's your name? ")
print("hello,", end="")
print(name)

#Formatting strings
name = input("What's your name? ")
print(f"hello,{name}")

#Strings
#strip method
name = input("What's your name? ")
name = name.strip()
print(f"hello,{name}")

#title method
name = input("What's your name? ")

name = name.strip()

name = name.title()

print(f"hello, {name}")

#Integer or int

x =  input("What's X? ")
y =  input("What's y? ")

z = int(x) + int(y)
print(z)

x = int(input("What's X? "))
y = int(input("What's y? "))
print(x+y)

#Float Basics
x = float(input("What's X? "))
y = float(input("What's y? "))
print(x+y)

x = float(input("What's X? "))
y = float(input("What's y? "))

z = round(x+y)
print(z)

x = float(input("What's X? "))
y = float(input("What's y? "))

z = round(x+y)
print(f"{z:,}")

x = float(input("What's X? "))
y = float(input("What's y? "))
z = x/y
print(z)

x = float(input("What's X? "))
y = float(input("What's y? "))

z = round(x/y,2)
print(z)

x = float(input("What's X? "))
y = float(input("What's y? "))

z = x/y
print(f"{z:.2f}")

#def
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

def hello(to):
    print("hello,",to)

name = input("What's your name? ")
hello(name)

def hello(to="world"):
    print("hello,",to)

name = input("What's your name? ")
hello(name)

hello()

def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="world"):
    print("hello,",to)

main()
#returning value
def main():
    x = int(input("What's X? "))
    print("x squared is", square(x))

def square(n):
    return n*n
main()
#IndoorVoice
s = input("What's your name? ")
print(s.lower())

#Playback speed

s = input()
print(s.replace(" ", "..."))

#Making Faces

def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s

def main():
    s = input()
    print(convert(s))

main()

#Einstien

m = int(input())
c = 300000000
E = m * c ** 
print(E)

#Tip Calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d[1:])

def percent_to_float(p):
    return float(p[:-1]) / 100

main()
