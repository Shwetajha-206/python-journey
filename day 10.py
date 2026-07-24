# import math

# class Solution:
#     def calculateArea(self, r):
#         area = round(math.pi * r * r * 5)
#         return area

# obj = Solution()
# print(obj.calculateArea(5))



# def isLeapYear(n):
#     if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
#         return True
#     else:
#         return False

# print(isLeapYear(2000))
# print(isLeapYear(1900))
# print(isLeapYear(2024))

# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#         return True

# print(isPrime(20))

def sumofDigit(n):
    total = 0
    while n > 0:
        digit = n%10
        total = total+digit
        n = n//10
    return total

print(sumofDigit(1234))

