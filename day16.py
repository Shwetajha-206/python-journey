#SEARCH A 2D MATRIX
# from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows = len(matrix)
#         cols = len(matrix[0])
#         low = 0
#         high = rows * cols - 1
#         while low <= high:
#             mid = (low + high) // 2
#             row = mid // cols
#             col = mid % cols
#             value = matrix[row][col]
#             if value == target:
#                 return True
#             elif value < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return False

# obj = Solution()
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# print(obj.searchMatrix(matrix, 3))    
# print(obj.searchMatrix(matrix, 13))   


#MATRIX DIAGONAL SUM
# from typing import List

# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n = len(mat)
#         total = 0
#         for i in range(n):
#             total += mat[i][i]
#             if i != n - 1 - i:
#                 total += mat[i][n - 1 - i]
#         return total

# obj = Solution()
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# print(obj.diagonalSum(mat))  

#TRANSPOSE MATRIX
# from typing import List

# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         rows = len(matrix)
#         cols = len(matrix[0])
#         result = [[0] * rows for _ in range(cols)]
#         for i in range(rows):
#             for j in range(cols):
#                 result[j][i] = matrix[i][j]
#         return result

# obj = Solution()
# print(obj.transpose([[1,2,3],[4,5,6]]))   

#TOEPLITZ MATRIX
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows - 1):
            for j in range(cols - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

obj = Solution()
print(obj.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])) 
print(obj.isToeplitzMatrix([[1,2],[2,2]]))                      