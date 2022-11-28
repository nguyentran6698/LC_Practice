def solution(root):
    res = 0

    def dfs(node):
        if node == None:
            return 0
        nonlocal res
        res += node.val
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


def solution2(root):
    res = 0
    if root == None:
        return res

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        res += node.val
        stack.append(node.left)
        stack.append(node.right)

    return res
