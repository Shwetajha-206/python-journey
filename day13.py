# from typing import List

# class Solution:
#     def findNonMinOrMax(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return -1
        
#         smallest = min(nums)
#         largest = max(nums)
        
#         for num in nums:
#             if num != smallest and num != largest:
#                 return num
        
#         return -1


# obj = Solution()
# print(obj.findNonMinOrMax([3, 2, 1, 4]))    
# print(obj.findNonMinOrMax([1, 2]))          
# print(obj.findNonMinOrMax([2, 1, 3]))       

# from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1

# obj = Solution()
# arr = ["h","e","l","l","o"]
# obj.reverseString(arr)
# print(arr)   # Output: ['o', 'l', 'l', 'e', 'h']

# from typing import List

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         expected_sum = n * (n + 1) // 2
#         actual_sum = sum(nums)
#         return expected_sum - actual_sum

# obj = Solution()
# print(obj.missingNumber([3, 0, 1]))   
# print(obj.missingNumber([0, 1]))       


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

obj = Solution()
arr = [0, 1, 0, 3, 12]
obj.moveZeroes(arr)
print(arr)   