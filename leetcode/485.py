# Problem: https://leetcode.com/problems/max-consecutive-ones/
    # Solution for 1 pass
def findMaxConsecutiveOnes1(nums) -> int:
    currMax = 0
    res = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            currMax += 1
        else:
            res = max(res,currMax)
            currMax = 0
    res = max(res,currMax)
    return res
    
# Solution 2: Sliding window
def findMaxConsecutiveOnes2(nums) -> int:
    l = r = 0
    n = len(nums)
    count = 0
    while l < n and r < n:
        while l < n and nums[l] == 0:
            l += 1
        r = l
        while r < n and nums[r] == 1:
            r += 1
        # store it
        count = max(count , r - l)
        l = r
    return count
print(findMaxConsecutiveOnes2([0,0,1,0,1,1,0,1]))