class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        seen = set()
        rows_seen = set()
        cols_seen = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_seen.add(r)
                    cols_seen.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in rows_seen or c in cols_seen:
                    matrix[r][c] = 0
                
        