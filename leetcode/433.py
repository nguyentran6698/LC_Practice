# URL: https://leetcode.com/problems/minimum-genetic-mutation/


from collections import deque
from collections import defaultdict
def minMutation(start, end, bank):
    q = deque([(start,0)])
    v = {start}

    while q:
        node,steps = q.popleft()
        if node == end:
            return steps
        
        for x in "ACGT":
            for i in range(len(node)):
                neighbor = node[:i] + x + node[i+1:]
                if neighbor not in v and neighbor in bank:
                    q.append((neighbor,steps + 1))
                    v.add(neighbor)
    return -1

# New Approach without permutation
def minMutation2(start,end,bank):
    d = defaultdict(int)
    d[start] = 0
    q = deque([start])

    while q:
        node = q.popleft()
        for v in bank:
            if v in d and d[v] != 0:
                continue
            cnt = 0
            for i in range(len(start)):
                if node[i] != v[i]:
                    cnt += 1
            if cnt == 1:
                d[v]  = d[node] + 1
                q.append(v)
    if end in d:
        return d[end]
    return -1







######################
#   Test Case       ##
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
print(minMutation2(start, end, bank))


