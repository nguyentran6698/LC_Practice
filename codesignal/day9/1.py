def solution(numbers, left, right):
    res = [] 
    for i in range(len(numbers)):
        if numbers[i] % (i + 1) != 0:
            res.append(False)
        else:
            x = numbers[i] // (i + 1)
            if left <= x <= right:
                res.append(True)
            else:
                res.append(False)
    return res 
