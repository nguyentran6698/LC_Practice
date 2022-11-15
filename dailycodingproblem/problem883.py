# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

from collections import deque


def divisors(n:int):
    res = []
    for i in range(int(n ** 0.5) , 1 , -1):
        if n % i == 0:
            res.append(n // i)
    return res

def solution(n:int):
    visited = set()
    queue = deque()
    queue.append((n,0))
    while queue:
        num,moves = queue.popleft()
        visited.add(num)

        if num == 1:
            return moves
        
        candiates = divisors(num) + [num - 1]
        for c in candiates:
            if c not in visited:
                queue.append((c,moves + 1))
    return -1

print(solution(100))