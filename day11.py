# def reverse(x):
#     if x<0:
#         sign = -1
#         x = -x
#     else:
#         sign = 1
#     reversed_num =0
#     while(x>0):
#         digit = x%10
#         reversed_num = reversed_num*10+digit
#         x = x//10
#     return reversed_num*sign
# x = -123
# print(reverse(x)) 

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)
# print(fibonacci(4))

# def isPalindrome(x):
#     if x < 0:
#         return False
    
#     original = x
#     reversed_num = 0
#     while(x > 0):
#         digit = x % 10
#         reversed_num = reversed_num * 10 + digit
#         x = x // 10
    
#     return original == reversed_num

# print(isPalindrome(123))

# def isHappy(n):
#     seen = set()
    
#     while n != 1:
#         if n in seen:
#             return False
#         seen.add(n)
        
#         total = 0
#         while n > 0:
#             digit = n % 10
#             total = total + digit * digit
#             n = n // 10
        
#         n = total
    
#     return True


# print(isHappy(19)) 
# print(isHappy(2))    


def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result
print(factorial(5))


