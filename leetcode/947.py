def solution(stones):
    n = len(stones)
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if stones[i][0] == stones[j][1] or stones[i][1] == stones[j][1]:
                g[i].append(j)
                g[j].append(i)
    vis = [0] * n
    cnt = 0
    def dfs(stones,graph,vis,src):
        vis[src] += 1
        for i in graph[src]:
            if vis[i] == 0:
                dfs(stones,graph,vis,i)
    for i in range(n):
        if vis[i] == 0:
            cnt += 1
            dfs(stones,g,vis,i)
    return n - cnt

# DSU
def solutin3(stones):
    # DSU
    parent = [i for i in range(len(stones))]
    size = [1  for _ in range(len(stones))]
    def sameRowOrColumn(a,b):
        return a[0] == b[0] or a[1] == b[1]
    def find_set(parent,x):
        if x == parent[x]:
            return x
        parent[x] = find_set(parent,parent[x])
        return parent[x]
    def union(parent,size,x,y):
        x = find_set(parent,x)
        y = find_set(parent,y)
        if x == y:
            return 0
        if size[x] > size[y]:
            parent[y] = x
            size[x] += size[y]
        else:
            parent[x] = y
            size[y] += size[x]
        return 1
    cnt = len(stones)
    for i in range(len(stones)):
        for j in range(i+1 , len(stones)):
            if(sameRowOrColumn(stones[i] , stones[j])):
                cnt -= union(parent,size,stones[i],stones[j])
    return len(stones) - cnt
        
        
def solution2(stones):
    K = 10001
    n = len(stones)
    g = [[] for _ in range(2*K +1)]
    for i in range(n):
        x = stones[i][0]
        y = stones[i][1] + K
        g[x].append(y)
        g[y].append(x)
    vis = [0] * (2 * K + 1)
    cnt = 0
    def dfs(stones,graph,vis,src):
        vis[src] += 1
        for i in graph[src]:
            if vis[i] == 0:
                dfs(stones,graph,vis,i)
    for i in range(2*K+1):
        if vis[i] == 0 and len(g[i]) > 0:
            cnt += 1
            dfs(stones,g,vis,i)
    return n - cnt


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(solutin3(stones))