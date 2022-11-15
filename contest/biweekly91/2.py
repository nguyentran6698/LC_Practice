from collections import defaultdict
from functools import cache
def solution(low: int, high: int, zero: int, one: int):
    MOD = int(1e9) + 7
    @cache
    def dp(idx):
        # print(idx)
        if idx == 0:
            return 1
        ret = 0
        if idx >= zero:
            ret += dp(idx - zero) # 2
        if idx >= one:
            ret += dp(idx - one) # 4
        ret %= MOD
        print(ret)
        return ret
    ret = 0
    for i in range(low , high + 1):
        ret += dp(i)
        ret %= MOD
    return ret
low = 3
high = 3
zero = 2
one = 1
solution(low,high,zero,one)