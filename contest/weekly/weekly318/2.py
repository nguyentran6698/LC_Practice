from collections import defaultdict
def solution(nums,k):
    curMax = 0
    start =  0
    maxVal = 0
    d = defaultdict(int)
    for end in range(len(nums)):
        curMax += nums[end]
        d[nums[end]] += 1
        while d[nums[end]] > 1:
            curMax -= nums[start]
            d[nums[start]] -= 1
            start += 1
        if end - start + 1>= k:
            maxVal = max(maxVal,curMax)
            curMax -= nums[start]
            d[nums[start]] -= 1
            start += 1
    return maxVal


print(solution([9,18,10,13,17,9,19,2,1,18],5))