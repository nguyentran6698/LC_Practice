class UnionFind:
    def __init__(self,arr) -> None:
        self.parent = arr
        self.n = len(arr)
    def initialize(self):
        for i in range(self.n):
            self.make_set(i)
    def make_set(self,v:int):
        self.parent[v] = v
    def find_set(self,v):
        if(v == self.parent[v]):
            return v
        return self.find_set(self.parent[v])

    def union_set(self,a,b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            self.parent[b] = a

def solution():
    arr = [0,1,2,3,4]
    s1 = UnionFind(arr)
    s1.initialize()
    s1.union_set(2,1)
    s1.union_set(4,3)
    print(s1.parent)
solution()

