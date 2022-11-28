class Solution(object):
    def canJump(self, nums):
        # backtrack solution

        def canJumpFromPosition(pos, nums):
            if pos == len(nums) - 1:
                return True

            longestJump = min(pos + nums[pos], len(nums) - 1)
            for nextPos in range(pos + 1, longestJump + 1):
                if canJumpFromPosition(nextPos, nums):
                    return True
            return False

        return canJumpFromPosition(0, nums)

        # Greedy solution
        # mx = 0
        # for i in range(len(nums)):
        #     if i > mx:
        #         return False
        #     if i == len(nums) - 1:
        #         return True
        #     mx = max(nums[i] + i , mx)
    