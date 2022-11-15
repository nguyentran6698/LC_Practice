import math
def solution(nums,k):
    ret = 0
    for i in range(len(nums)):
        lcm = 1
        for j in range(i,len(nums)):
            lcm = math.lcm(lcm,nums[j])
            print(lcm)
            if lcm == k:
                ret += 1
    return ret

    #[2,1,1,5] -> 6
    #[3,6,2,7,1] = 6
print(solution([2,1,1,5],5))
            