import math
def solution(t1,t2,p):
    n1 = n2 = 0
    if t1 > t2:
        t2,t1 = t1,t2
    n2 = math.ceil(p / t2)
    while n2 > -1:
        if n2 * t2 > p:
            n2 -= 1
            continue
        x = p - (n2 *t2)
        if x >= t1 and x % t1 == 0:
            n1 = x // t1
            break
        else:
            n2 -= 1
    return n1 + n2

print(solution(4,4,9))
        