from typing import List
class UF:
    def __init__(self,n):
        self.p = [-1 for i in range(n +1)]
    def find(self,v):
        if self.p[v] == -1:
            return v
        return self.find(self.p[v])
    def union(self,node,parent):
        s1 , s2 = self.find(node) , self.find(parent)
        if s1 != s2:
            self.p[s1] = s2
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)
        for i in range(n):
            graph = isConnected[i]
            parent = i + 1
            for idx,node in enumerate(graph):
                if (idx + 1) != parent and node == 1:
                    uf.union(idx + 1,parent)
            
            cnt = 0
            for i in range(1,len(uf.p)):
                if uf.p[i] == -1:
                    cnt += 1
        return cnt   