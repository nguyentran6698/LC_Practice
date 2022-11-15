from typing import List
def solution(nums: List[int]):
    avg = set()
    nums.sort()
    for i in range(len(nums) // 2):
        avg.add((nums[i] + nums[len(nums) - 1 - i]) // 2)
        print(avg)
    return len(avg)

print(solution([4,1,4,0,3,5]))

