def solution(numbers):
    a = max(numbers)
    cd = []
    curr = 0
    i = 0
    cnt = 0
    while curr <= (a+a):
        cd.append(curr)
        i += 1
        curr = pow(i,2)
    for k in cd:
        key_match = set()
        for num in numbers:
            key_match.add(num)
            if (k - num) in key_match:
                cnt += 1
    return cnt

numbers = [-20000, 20000, 0, 1, 4, 9, 16]
print(solution(numbers))

# 0 1 4 9 16 25 
# 2 3 4 5 

