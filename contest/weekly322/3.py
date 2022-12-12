def solution(n,roads):
    g = [[] for _ in range(n)]
    ret = float('inf')
    for x,y,z in roads:
        x -= 1
        y -= 1
        g[x].append((y,z))
        g[y].append((x,z))
    vis = set()
    def dfs(idx):
        nonlocal ret
        vis.add(idx)
        for o,w in g[idx]:
            ret = min(ret,w)
            if o not in vis:
                dfs(o)
    dfs(0)
    return ret

n = 7
roads = [[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]
print(solution(n,roads))
