def solution(numbers, left, right):
    res = [False] * len(numbers)
    for i in range(len(numbers)):
        if numbers[i] % (i+1) == 0:
            x = numbers[i] / (i+1)
            if left <= x <= right:
                res[i] = True
           
    return res 
            
