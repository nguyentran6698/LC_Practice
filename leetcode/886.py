class UF:
    def __init__(self,n):
        self.p = [i for i in range(n+1)]
    def find(self,v):
        if self.p[v] == v:
            return v
        return self.find(self.p[v])
    
    def union(self, a1, a2):
        a1 = self.find(a1)
        self.p[a1] = a2
    
def solution(n,dislike):
    g = [[] for i in range(n+1)]
    uf = UF(n)
    for x,y in dislike:
        g[x].append(y)
        g[y].append(x)
    
    # check for each node
    for i in range(1,n+1):
        parent = uf.find(i)
        if len(parent):
            parent_dislike = uf.find(g[i][0])
            for j in g[i][1:]:
                uf.union(j,parent_dislike)
                if parent == uf.find(j):
                    return False
    return True

class Solution:
    def dfs(self, i, group):
        if i in self.group_mapping and group != self.group_mapping[i]:   # Check if there is a conflict
            return False                                                 # between given group and existing group
        self.group_mapping[i] = group
        if i not in self.visited:
            self.visited.add(i)
            for dis in self.graph[i]:                                    # DFS for each dislike node recursively
                if not self.dfs(dis, not group): return False            # Assign contrary group to dislike node
        return True    
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        self.visited, self.group_mapping = set(), {}
        for (u, v) in dislikes:                                          # Create graph 
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):                                          # DFS until eror
            if i not in self.visited:                                    # We don't want to revisit since it's DFS
                if not self.dfs(i, True):                                # If conflict occurs during DFS, return False
                    return False
        return True

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        group_mapping = {}
        for (u, v) in dislikes:                             # Create graph
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        visited = set()
        for i in range(1, N + 1):                           # Iterate each node
            if i in visited: continue                       # No need to revisit, since it's a non-directed graph
            stack = [(i, 0)]                                # Use stack for BFS
            while stack:                                    # You can also use a deque instead of 2 while loop on stack
                tmp_stack = []
                while stack:                                # exhaust current stack before go to next layer (BFS)
                    cur_node, group = stack.pop()
                    if cur_node in group_mapping and group != group_mapping[cur_node]:  # check if it's conflict
                        return False
                    if cur_node in visited: continue        # If visited and no conflict, continue to avoid dead loop
                    group_mapping[cur_node] = group         # Assign group for current node
                    visited.add(cur_node)
                    for child in self.graph[cur_node]:      # Assign contrary group for dislikes of current node
                        tmp_stack.append((child, not group))
                stack = tmp_stack            
        return True   