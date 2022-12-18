from typing import List
# HashValue
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            if num - 1 not in s:
                curr = num 
                cnt = 1
                while curr + 1 in s:
                    curr += 1
                    cnt += 1

                res = max(res,cnt)
        return res

# Union Find
class UnionFind:
    def __init__(self,nums):
        self.nums = {num: num for num in nums}
        self.rank = {num: 1 for num in nums}
    def find(self,v)->int:
        if v == self.nums[v]:
            return v
        return self.find(self.nums[v])
    
    def union_set(self,a1,a2):
        s1,s2 = self.find(a1) , self.find(a2)
        if s1 != s2:
            if self.rank[s1] > self.rank[s2]:
                self.nums[s2] = s1
                self.rank[s1] += self.rank[s2]
            else:
                self.nums[s1]  = s2
                self.rank[s2] += self.rank[s1]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Union find
        uf = UnionFind(set(nums))

        for num in uf.nums:
            if num - 1 in uf.nums:
                uf.union_set(num,num-1)
            if num + 1 in uf.nums:
                uf.union_set(num,num+1)
        return max(uf.rank.values()) if nums else 0
            