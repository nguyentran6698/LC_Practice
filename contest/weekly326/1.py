def solution(num):
    cnt = 0
    for n in str(num):
        if num % int(n) == 0:
            cnt += 1
    return cnt


print(solution(121))
