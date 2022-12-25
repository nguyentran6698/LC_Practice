from typing import List
import bisect
def solution2( nums: List[int], queries: List[int]) -> List[int]:
    ans = []
    nums.sort()
    for i in range(len(queries)):
        cnt = 0
        curr = 0
        for s in nums:
            if curr + s < queries[i]:
                cnt += 1
                curr += s
            else:
                break
        ans.append(cnt)
    return max(ans)


# PrefixSum and Binary Search
def solution1(nums: List[int], queries: List[int]) -> List[int]:
    nums.sort()
    p = [0] * len(nums)
    res = []
    # prefixSum array
    p[0] = nums[0]
    for i in range(1,len(nums)):
        p[i] = nums[i] + p[i-1]

    for query in queries:
        index = bisect.bisect_right(p,query)
        res.append(index)
    return res
nums = [4,5,2,1]
queries = [3,10,21]
print(solution1(nums,queries))