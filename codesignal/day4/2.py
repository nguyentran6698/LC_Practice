from collections import defaultdict
def solution(a):
    ret = []
    res = [0] * 101
    for num in a:
        while num > 0:
            num,digit = divmod(num,10)
            res[digit] +=  1
    maxV = max(res)
    for i in range(0,101):
        if res[i] == maxV:
            ret.append(i)
    return ret

a = [1, 10, 20, 10, 30]
print(solution(a))