class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix):
            return False
        i, j = 0, 0
        m = len(matrix)
        n = len(matrix[0])
        while i < m:
            if matrix[i][0] <= target and target <= matrix[i][n-1]:
                while j < n:
                    if matrix[i][j] == target:
                        return True
                    j += 1
                break
            i += 1
    
        return False
