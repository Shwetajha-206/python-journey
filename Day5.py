# list = [5,2,8,1,9]
# list.append(10)
# print(list)

# list.insert(0,100)
# print(list)

# list.remove(2)
# print(list)

# list.pop()
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)

# print(list)

# arr = [1,2,3,4,5,6,7,8,9,10]
# print(arr[2:5])
# print(arr.count(3))

# my_tuple = (1,2,3,4,5)
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[2:5])
# print(len(my_tuple))
# print(my_tuple.count(3))
# my_tuple[0] = 100

# List to tuple
# my_list = [1,2,3,4,5]
# converted_tuple = tuple(my_list)
# print(converted_tuple)
# print(type(converted_tuple))

#Tuple to list

# my_tuple = (1,2,3,4,5)
# converted_list = list(my_tuple)
# print(converted_list)
# print(type(converted_list))

# my_tuple = (1,2,3,4,5)
# temp_list = list(my_tuple)
# temp_list.append(6)
# print(temp_list)

# final_tuple = tuple(temp_list)
# print(final_tuple)

#Dictionary
# my_self = {"name": "Shweta","age":20,}
# print(my_self)

# my_self["city"] = "Delhi"
# print(my_self)

# my_self["age"] = 19
# print(my_self)

# del my_self["city"]
# print(my_self)

# print(my_self.keys())
# print(my_self.values())
# print(my_self.items())

#sets

# x = {1,2,3}
# y = {3,4,5}
# print(x.union(y))
# print(x.intersection(y))
# print(x.difference(y))


# names = ["priya","rahul","priya","amit","rahul"]
# unique_names = list(set(names))
# print(unique_names)

#Exception Handling
# try:
#     x = int(input("Enter a number:"))
#     result = 10/x
# except ZeroDivisionError:
#     print("Divide by zero nhi kr skte")
# except ValueError:
#     print("Shi number daalo")
# finally:
#     print("Yeh hmesha chlega")

# for i in range(1,5):
#     print(i)
# else:
#     print("loop complete hua")

# numbers = [10,20,30,40,50]
# search = 30

# for num in numbers:
#     if(num == search):
#         print("Number mil gya:",num)
#         break
# else:
#     print("Number nahi mila")

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n*factorial(n-1)
# result = factorial(5)
# print(result)


def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
result = fibonacci(6)
print(result)

def sum_of_digits(n):
    if(n==0):
        return 0
    else:
        return (n%10) + sum_of_digits(n//10)
    
result = sum_of_digits(123)
print(result)