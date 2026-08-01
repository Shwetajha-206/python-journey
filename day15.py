#SORT COLORS
# from typing import List

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         low = 0
#         mid = 0
#         high = len(nums) - 1
#         while mid <= high:
#             if nums[mid] == 0:
#                 nums[low], nums[mid] = nums[mid], nums[low]
#                 low += 1
#                 mid += 1
#             elif nums[mid] == 1:
#                 mid += 1
#             else:
#                 nums[mid], nums[high] = nums[high], nums[mid]
#                 high -= 1

# obj = Solution()
# arr = [2, 0, 2, 1, 1, 0]
# obj.sortColors(arr)
# print(arr)  

#MAJORITY ELEMENT
# from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         for num in nums:
#             if num in count:
#                 count[num] += 1
#             else:
#                 count[num] = 1
#         for key in count:
#             if count[key] > len(nums) // 2:
#                 return key

# obj = Solution()
# print(obj.majorityElement([3, 2, 3]))             
# print(obj.majorityElement([2,2,1,1,1,2,2]))  

# MAX SUBARRAY   

# from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         current_sum = nums[0]
#         max_sum = nums[0]
#         for i in range(1, len(nums)):
#             current_sum = max(nums[i], current_sum + nums[i])
#             max_sum = max(max_sum, current_sum)
#         return max_sum

# obj = Solution()
# print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))     

class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for num in arr:
            needed = target - num
            if needed in seen:
                return True
            seen.add(num)
        return False

obj = Solution()
print(obj.twoSum([0, -1, 2, -3, 1], -2))  
print(obj.twoSum([1, -2, 1, 0, 5], 0))      
print(obj.twoSum([11], 11))                 