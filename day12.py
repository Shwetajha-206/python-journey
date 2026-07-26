# class Solution:
#     def rotateArray(self, arr, d):
#         self.reverse(arr, 0, d-1)
#         self.reverse(arr, d, len(arr)-1)
#         self.reverse(arr, 0, len(arr)-1)
#         return arr
    
#     def reverse(self, arr, start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1


# # TEST KARNE KE LIYE
# sol = Solution()
# arr = [1, 2, 3, 4, 5]
# d = 2

# result = sol.rotateArray(arr, d)
# print(result)


# class Solution:
#     def subArrays(self, arr):
#         result = []
#         for i in range(0, len(arr)):
#             for j in range(i, len(arr)):
#                 result.append(arr[i:j+1])
#         return result

# sol = Solution()
# arr = [1, 2, 3]

# result = sol.subArrays(arr)
# print(result)

class Solution:
    def moveZeroes(self, arr):
        insert_pos = 0
        for i in range(0, len(arr)):
            if arr[i] != 0:
                arr[insert_pos] = arr[i]
                insert_pos += 1
        
        for i in range(insert_pos, len(arr)):
            arr[i] = 0
        
        return arr

sol = Solution()
arr = [0, 1, 0, 3, 12]

result = sol.moveZeroes(arr)
print(result)