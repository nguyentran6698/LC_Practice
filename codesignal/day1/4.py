def solution(numbers):
    v = max(numbers)
    idx = 0
    cnt = 0
    d = set()
    dv = {}
    for i in range(len(numbers)):
        dv[numbers[i]] = i
    
    while pow(2,idx) <= (v * 2):
        d.add(pow(2,idx))
        idx += 1
    setN = set(numbers)
    for i in range(len(numbers)):
        curr = numbers[i] 
        for w in d:
            if (w - curr) in setN and dv[w - curr] >= i:
                cnt += 1
    return cnt

print(solution([-2,-1,0,1,2]))

# Solution with O(32n)
def solution2(numbers):
    cnt = 0
    for i in range(32):
        
        key = 2 ** i
        key_map = set()

        for num in numbers:
            key_map.add(num)
            if (key - num) in key_map:
                cnt += 1
    return cnt
print(solution2([2]))
