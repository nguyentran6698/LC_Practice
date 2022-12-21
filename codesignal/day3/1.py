def solution(numbers):
    res = []
    for i in range(len(numbers)  - 2):
        if (numbers[i] < numbers[i + 1] > numbers[i+2]) or (numbers[i] > numbers[i+1] < numbers[i+2]) :
            res.append(1)
        else:
            res.append(0)
            
    return res
            
