def findMaxConsecutiveOnes(nums)->int:
    flips = 1
    ans = r = l = 0
    n = len(nums)
    while r < n:
        flips -= 1 - nums[r]
        while flips < 0:
            flips += 1 - nums[l]
            l += 1
        ans = max(ans , r - l + 1)
        r += 1
    return ans

# Seperate 
def findMaxConsecutiveOnes2(nums)->int:
    lst = None 
    ct = 0
    l = []
    for num in nums:
        if num != lst:
            if lst is not None:
                l.append((num,ct))
            lst = num
            ct = 1
        else:
            ct += 1
    l.append((lst,ct))
    ret = 1
    for i,(x,y) in enumerate(l):
        if x == 1:
            ret = max(ret,y)
        if x == 0:
            q = 1
            if i > 0:
                q += l[i-1][1]
                ret = max(ret,l[i-1][1] + 1)
            if i < len(l) - 1:
                q += l[i+1][1]
                ret = max(ret,l[i+1][1] + 1)
            if y == 1:
                ret = max(ret,q)
    return ret



print(findMaxConsecutiveOnes2([1,0,1,1,0]))
