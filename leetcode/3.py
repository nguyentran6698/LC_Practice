from collections import defaultdict
# def solution1(s: str) -> int:
#     # Solution 2: Sliding Windows
#     end = start = 0
#     res = 0 
#     d = defaultdict(int)
#     currentMax = 0
#     while end < len(s):
#         ch = s[end]
#         d[ch] += 1
#         while d[ch] > 1:
#             l = s[start]
#             d[l] -= 1
#             start += 1
        
#         res =  max(res , end - start + 1)
#         end += 1
#     return res 
# Optimization 
def solution2(s):
    i = 0 
    d = {}
    res = 0
    for j in range(len(s)):
        if  s[j] in d:
            i = max(i , d[s[j]])
        res = max(res,j - i + 1)
        d[s[j]] = j + 1
    return res
print(solution2("abcabcbb"))


# a b c a b c b b
# i i i i   i   i
# j j j j j j j
# d{a: 4 , b: 7 , c: 6 }

# 