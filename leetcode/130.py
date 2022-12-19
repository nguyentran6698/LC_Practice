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
    def solve(self, board: List[List[str]]) -> None:
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]
        def union_set(a1,a2):
            s1,s2 = find(a1), find(a2)
            if s1 != s2:
                parent[s2] = s1
        
        if len(board) <= 1:
            return 
        rows = len(board)
        cols = len(board[0])
        parent = {i:i for i in range(rows*cols + 1)}
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        union_set(i*rows+j , rows * cols)
                    else:
                        if board[i - 1][j] == "O":
                            union_set((i-1)*cols + j , i * cols + j)
                        if board[i + 1][j] == "O":
                            union_set((i+1)*cols + j , i * cols + j)
                        if board[i][j-1] == "O":
                            union_set(i*cols+(j-1),i *cols + j)
                        if board[i][j+1] == "O":
                            union_set(i*cols+(j+1) , i * cols + j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and find(i*cols + j) != find(rows*cols):
                    board[i][j] = "X"
        
