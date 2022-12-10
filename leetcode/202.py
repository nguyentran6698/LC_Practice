def solution(n):
    
    def get_nxt(n):
        total = 0
        while n > 0:
            n,r = divmod(n,10)
            total += pow(r,2)
        return total
    
    slow = n
    fast = get_nxt(n)
    while fast != 1 and fast != slow:
        slow = get_nxt(slow)
        fast = get_nxt(get_nxt(fast))
    return fast == 1
print(solution(2))