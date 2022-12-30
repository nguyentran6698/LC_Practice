def solution(a):
    res = []
    if len(a) == 1:
        return a
    for i in range(len(a)):
        if i == 0 :
            res.append(0 + a[i] + a[i+1])
        elif i == len(a) - 1:
            res.append(a[i-1] + a[i] + 0)
        else:
            res.append(a[i-1] + a[i] + a[i+1])        
    return res 
a =  [1, 2, 3, 4]
print(solution(a))
