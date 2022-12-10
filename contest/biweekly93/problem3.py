class Solution:
    def maxJump(self, stones: List[int]) -> int:
        l = 0
        n = len(stones)
        for i in range(n - 1):
            l = max(stones[i + 1] - stones[i], l)
        r = stones[-1] - stones[0]

        def can(x):
            vis = [0] * n
            idx = 0
            while idx != n - 1:
                idx = bisect.bisect(stones, stones[idx] + x) - 1
                vis[idx] = 1
            cur = stones[-1]
            for i in range(n - 1, -1, -1):
                if not vis[i]:
                    diff = cur - stones[i]
                    if diff > x:
                        return False
                    cur = stones[i]
            return True

        while l < r:
            m = l + (r - l) // 2
            if can(m):
                r = m
            else:
                l = m + 1
        return r
