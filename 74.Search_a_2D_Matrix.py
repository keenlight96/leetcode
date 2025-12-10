from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # edge cases
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        row_top = 0
        row_btm = len(matrix) - 1
        col_left = 0
        col_right = len(matrix[0]) - 1
        row_mid = (row_top + row_btm) // 2
        col_mid = (col_left + col_right) // 2
        
        while row_top <= row_btm and col_left <= col_right:
            mid = matrix[row_mid][col_mid]
            if matrix[row_mid][col_mid] == target:
                return True
            elif matrix[row_mid][0] > target:
                row_btm = row_mid - 1
            elif matrix[row_mid][-1] < target:
                row_top = row_mid + 1
            else:
                if matrix[row_mid][col_mid] > target:
                    col_right = col_mid - 1
                else:
                    col_left = col_mid + 1
            row_mid = (row_top + row_btm) // 2
            col_mid = (col_left + col_right) // 2
        return False

solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# target = 13
print(solution.searchMatrix(matrix, target))