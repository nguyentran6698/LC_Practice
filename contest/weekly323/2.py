class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # 2 3 4 6 8 16
        ret = -1
        s = set(nums)
        for num in nums:
            cn = num
            for i in range(2, 10**5 + 1):
                cn *= cn
                if cn in s:
                    ret = max(ret,i)
                else:
                    break
        return ret
                    