def solution(s, k):
    l = [int(i) for i in s]
    res = 0
    curr = 0
    for num in l:
        temp = curr * 10 + num
        if temp > k:
            res += 1
            curr = num
        else:
            curr = temp
    return res + 1


s = "165462"
k = 60
print(solution(s, k))
