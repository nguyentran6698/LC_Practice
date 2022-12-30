def solution(grid):
    ans = 0
    m = len(grid[0])
    n = len(grid)
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(m - 1, -1 ,-1):
        curr = 0
        for j in range(n):
            curr = max(curr,grid[j][i])
        ans += curr
    return ans
        
grid = [[1,2,4],[3,3,1]]
solution(grid)

# 1 2 4
# 1 3 3 
# 1 3 4