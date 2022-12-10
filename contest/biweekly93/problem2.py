import math


def solution(vals, edges, k):
    g = [[] for _ in range(len(edges) + 1)]
    N = len(edges)
    # construct the graph
    for i in range(N):
        x, y = edges[i]
        g[x].append(y)
        g[y].append(x)
    # dfs
    ss = list(range(N))
    print(ss)
    ss.sort(key=lambda x: -vals[x])


# Test case
vals = [1, 2, 3, 4, 10, -10, -20]
edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]
k = 2
solution(vals, edges, k)
