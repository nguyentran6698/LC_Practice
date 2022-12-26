def solution(numbers):
    res = []
    for i in range(1,len(numbers) - 1):
        if numbers[i - 1] < numbers[i] > numbers[i+1] or numbers[i-1] > numbers[i] < numbers[i+1]:
            res.append(1)
        else:
            res.append(0)
    return res 
        