from collections import defaultdict
def solution(root):
    # dfs first to map them into the dictionar
    depth = defaultdict(list)
    def dfs(node,d):
        depth[d].append(node)
        for ch in node.left , node.right:
            if ch:
                dfs(ch,d+1)
    dfs(root,0)
    ret = 0
    for k in depth:
        l = depth[k]
        r = sorted(l)
        m = {}
        for i,x in enumerate(l):
            m[x] = r[i]
        vis = set()
        for t in m:
            if t not in vis:
                q = 0
                cur = t
                while m[cur] not in vis:
                    vis.add(m[cur])
                    cur = m[cur]
                    q += 1
                ret += q  - 1
    return ret





   


    return ret



        