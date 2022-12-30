def solution(arr):
    if len(arr) < 2:
        return 0
    s = 0
    n = len(arr)
    e = 1
    cnt = 0
    def sameSign(a,b):
        if a/abs(a) == b/abs(b):
            return True
        return False
    
    while e < n:
        sign = arr[e] - arr[s]
        while (e < n  and arr[e] != arr[e - 1] and sameSign(arr[e] - arr[e-1] , sign)):
            sign = -1 * sign
            e += 1
        
        size = e - s
        if size == 1:
            e += 1
        cnt += (size * (size - 1)) // 2
        s = e - 1
        e = s + 1
    return cnt 