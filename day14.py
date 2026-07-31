# from typing import List


# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_count = 0
#         current = 0
#         for num in nums:
#             if num == 1:
#                 current += 1
#                 max_count = max(max_count, current)
#             else:
#                 current = 0
#         return max_count


# sol = Solution()
# print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])) 
# print(sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  




# from typing import List
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n

#         def reverse(left, right):
#             while left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1

#         reverse(0, n - 1)
#         reverse(0, k - 1)
#         reverse(k, n - 1)


# sol = Solution()

# nums1 = [1, 2, 3, 4, 5, 6, 7]
# sol.rotate(nums1, 3)
# print(nums1)  

# nums2 = [-1, -100, 3, 99]
# sol.rotate(nums2, 2)
# print(nums2)  


# from typing import List


# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
        
#         option1 = nums[n-1] * nums[n-2] * nums[n-3]
#         option2 = nums[0] * nums[1] * nums[n-1]
        
#         return max(option1, option2)


# sol = Solution()

# print(sol.maximumProduct([1, 2, 3]))        
# print(sol.maximumProduct([1, 2, 3, 4]))      
# print(sol.maximumProduct([-1, -2, -3]))      
# print(sol.maximumProduct([-10, -10, 1, 3, 2])) 

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k


sol = Solution()

nums1 = [1, 1, 2]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  