# Solution 1: My solution
def longestOnes1 (nums, k: int) -> int:
    l = r = 0
    currZero = 0
    n = len(nums)
    maxOne = 0
    while r < n:
        if nums[r] == 0:
            currZero += 1
        if currZero <= k:
            maxOne = max(maxOne,r - l + 1)
        while currZero > k:
            if nums[l] == 0:
                currZero -= 1
            l += 1
        
        r += 1
    return maxOne

# Solution 2: Sliding window more advance
def longestOnes2(nums,k:int)->int:
    l = 0
    for r in range(len(nums)):
        k -= 1 - nums[r]

        if k < 0:
            k += 1 - nums[l]
            l += 1
    return r - l + 1


        