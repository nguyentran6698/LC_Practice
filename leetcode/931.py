class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        res = inf
        def findMin(matrix,row,col):

            if col < 0 or col == len(matrix):
                return inf
            
            if row == len(matrix) - 1:
                return matrix[row][col]
            
            left = findMin(matrix, row + 1, col - 1)
            right = findMin(matrix, row + 1 , col + 1)
            middle = findMin(matrix, row + 1, col)

            return min(left,right,middle) + matrix[row][col]
        
        for col in range(len(matrix)):
            res = min(res,findMin(matrix,0,col))
        return res
