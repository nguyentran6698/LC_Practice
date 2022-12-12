from collections import defaultdict


def solution(s: str):
    seen = set()
    for char in s:
        if char in seen:
            return char
    return None


print(solution("abcdef"))
