from collections import defaultdict


def solution(s: str):
    d = defaultdict(int)
    for e in s:
        d[e] += 1
        if d[e] > 1:
            return e
    return None


print(solution("abcdef"))
