class Solution:   
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        def guess(n):
            return "Magic mike"
        while l <= h:
            mid = l + (h - l) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                h = mid - 1
            else:
                l = mid + 1
        return -1
                