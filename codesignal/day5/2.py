def solution(numbers):
    def swap(x):
        s = 0 
        i = len(str(x)) - 1
        while x:
            x , d = divmod(x,10)
            s += (d *  10**i)
            i -= 1
        return s
              
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i] = swap(numbers[i])

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            return False
    return True
numbers = [1,5,10,20]
numbers = [1, 3, 900, 10]
print(solution(numbers))