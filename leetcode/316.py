from collections import Counter
def solution(s):
    c = Counter(s)
    pos = 0
    for i in range(len(s)):
        # we found the one that we can chop
        if s[i] < s[pos]:
            pos = i
        c[s[i]] -= 1
        # we hit the element that need to be include
        if c[s[i]] == 0:
            break
    return s[pos] + solution(s[pos:].replace(s[pos],"")) if s else ""

print(solution("bccabe"))

# solution 2
def solution(s):
    stack = []
    seen = set()
    last_occurrence = {c: i for i, c in enumerate(s)}
    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)