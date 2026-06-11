#if statements

x = int(input("What's X? "))
y = int(input("What's Y? "))

if x<y:
    print("x is less than y")

#Control flow,elif and else
x = int(input("What's X? "))
y = int(input("What's Y?" ))
if x<y:
   print("X is less than y ")
if x>y:
   print("X is greater than y ")
if x==y:
   print("X is equal to y ")

x = int(input("What's X? "))
y = int(input("What's y? "))

if x<y:
    print("X is less than y")
elif x>y:
    print("X is greater than y")
elif x==y:
    print("X is equal to y")

x = int(input("What's X? "))
y = int(input("What's y? "))

if x<y:
    print("X is less than y")
elif x>y:
    print("X is greater than y")
else:
    print("X is equal to y")

#Or
x = int(input("What's X? "))
y = int(input("what's y? "))
if x<y or x>y:
    print("X is not equal to y")
else:
    print("X is equal to y")

x = int(input("What's X? "))
y = int(input("What's Y? "))

if x!=y:
    print("X is not equal to y")
else:
    print("X is equal to y")

x = int(input("What's x? "))
y = int(input("What's y? "))

if x==y:
    print("X is equal to y")
#else:
    #print("X is not equal to y")

#and
#score = int(input("Score: "))

#if score>=90 and score<=100:
    #print("Grade: A")
#elif score>=80 and score<90:
    #print("Grade: B")
#elif score>=70 and score<80:
   # print("Grade: C")
#elif score>=60 and score<70:
    #print("Grade: D")
#else:
    #print("Grade: F")


#Still, we can further improve our program:
#score = int(input("Score: "))

#if score >= 90:
    #print("Grade: A")
#elif score >= 80:
    #print("Grade: B")
#elif score >= 70:
    #print("Grade: C")
#elif score >= 60:
    #print("Grade: D")
#else:
    #print("Grade: F")

#x = int(input("What's X? "))
#if x % 2 == 0:
    #print("Even")
#else:
    #print("odd")

#Creating your own parity function
#def main():
    #x = int(input("What's X? "))
    #if is_even(x):
        #print("Even")
    #else:
        #print("odd")

#def is_even(n):
    #if n%2 == 0:
        #return True
    #else:
       # return False
#main()

#Pythonic

#def main():
    #x = int(input("What's x? "))
    #if is_even(x):
        #print("Even")
    #else:
        #print("Odd")


def is_even(n):
    return n % 2 == 0


main()

#Match
name = input("What's your name? ")

if name == "Harry":
      print("Gryffindor")
elif name == "Hermione":
     print("Gryffindor")
elif name == "Ron": 
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

#Alternatively, we can use match statements to map names to houses. Consider the following code:

name = input("What's your name? ")

match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

#We can improve the code:

name = input("What's your name? ")

match name: 
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")