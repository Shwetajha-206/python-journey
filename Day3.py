#loops 
# while Loop
i=3
while i!=0:
   print("meow")
i= i-1

#We can further improve our code as follow:
i=1
while i<=3:
    print("meow")
    i = i+1

i = 0
while i<3:
    print("meow")
    i+=1

#For loops
for i in [0,1,2]:
    print("meow")

for i in range(1,10):
    print("meow")

print("meow"*3)
print("meow\n"*3, end = "")

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


while True:
    n = int(input("What's n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

#List
students = ["Hermione","Harry","Ron"]
print(students[0])
print(students[1])
print(students[2])

students = ["Hermione","Harry","Ron"]
for student in students:
    print(student)

students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(students[i])

students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(i,students[i])


students = ["Hermione","Harry","Ron"]
for i in range(len(students)):
    print(i+1,students[i])

#Dictionaries


students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherine"
}

print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

students = {
    "Hermoine" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherine"
}

for student in students:
    print(student)

students = {
    "Hermoine" : "Gryffindor",
   "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherine"
}

for student in students:
   print(student, students[student], sep = ", "  )

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")



