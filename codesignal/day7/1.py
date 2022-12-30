def solution(a):
    b = [0] * len(a)
    if len(a) == 1:
        return a
    for i in range(len(a)):
        if i == 0 :
            b[i] = 0 + a[i] + a[i+1]
        elif i == len(a) - 1:
            b[i] = a[i-1] + a[i] + 0
        else:
            b[i] = a[i-1] + a[i] + a[i+1]
    return b
        

