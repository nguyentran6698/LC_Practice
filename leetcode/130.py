from itertools import product
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        borders = list(product(range(rows),[0,cols-1])) + list(product([0,rows - 1] , range(cols)))
        
        def dfs(board,row,col):
            if board[row][col] != "O":
                return
            board[row][col] = "E"
        
            if col < len(board[0]) - 1:
                dfs(board,row,col+1)
            if col > 0:
                dfs(board,row,col - 1)
            
            if row > 0:
                dfs(board,row - 1, col)
            if row < len(board) - 1:
                dfs(board,row + 1, col)

        for r,c in borders:
            dfs(board,r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] =="E":
                    board[r][c] = "O"
    # Union Ways
    # def solve(self, board: List[List[str]]) -> None:
