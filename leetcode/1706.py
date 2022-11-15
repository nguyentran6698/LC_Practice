def findBall(grid):
    r , c = len(grid) , len(grid[0])
    ret = [-1] * r 
    for j in range(c):
        cur = j
        for i in range(r + 1):
            if i == r:
                ret[j] = cur
            elif grid[i][cur] == 1:
                if cur == c - 1 or grid[i][cur + 1] == -1:
                    break
                cur += 1
            else:
                if cur == 0 or grid[i][cur-1] == 1:
                    break
                cur -= 1
    return ret

print(findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))