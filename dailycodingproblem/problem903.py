from collections import Counter 
def solution(nums,k):
    d = set()
    for i in range(len(nums)):
        r = k - i
        for j in range(i+1,len(nums)):
            if(r - nums[j]) in d:
                return True
            d.add(r - nums[j])
    return False 
print(solution([20, 303, 3, 4, 25],49))