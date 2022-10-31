from typing import List

class Solution:
    # First solution
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        return True

    # Second solution
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        length = len(matrix[0])

        for i in range(len(matrix) - 1):
            if matrix[i][:length - 1] != matrix[i + 1][1:]:
                return False

        return True