# #SEARCH A 2D MATRIX - II
# from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows = len(matrix)
#         cols = len(matrix[0])
#         row = 0
#         col = cols - 1
#         while row < rows and col >= 0:
#             if matrix[row][col] == target:
#                 return True
#             elif matrix[row][col] > target:
#                 col -= 1
#             else:
#                 row += 1
#         return False

# obj = Solution()
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# print(obj.searchMatrix(matrix, 5))   
# print(obj.searchMatrix(matrix, 20))   


# ROTATE IMAGE
# from typing import List

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for row in matrix:
#             row.reverse()

# obj = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# obj.rotate(matrix)
# print(matrix)   

#SPIRAL MATRIX
# from typing import List

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         result = []
#         top, bottom = 0, len(matrix) - 1
#         left, right = 0, len(matrix[0]) - 1
        
#         while top <= bottom and left <= right:
#             for col in range(left, right + 1):
#                 result.append(matrix[top][col])
#             top += 1
            
#             for row in range(top, bottom + 1):
#                 result.append(matrix[row][right])
#             right -= 1
            
#             if top <= bottom:
#                 for col in range(right, left - 1, -1):
#                     result.append(matrix[bottom][col])
#                 bottom -= 1
            
#             if left <= right:
#                 for row in range(bottom, top - 1, -1):
#                     result.append(matrix[row][left])
#                 left += 1
        
#         return result

# obj = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(obj.spiralOrder(matrix))  

#DIAGONAL TRAVERSE

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []
        diagonals = {}
        for i in range(rows):
            for j in range(cols):
                key = i + j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[i][j])
        for key in range(rows + cols - 1):
            if key % 2 == 0:
                result.extend(reversed(diagonals[key]))
            else:
                result.extend(diagonals[key])
        return result

obj = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(obj.findDiagonalOrder(mat))   