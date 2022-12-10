class Tree:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
def solution(root):
    if root == None:
        return 0
    ret = 0
    def dfs(node,maxNum ,minNum):
        nonlocal ret
        ret = max(ret,abs(maxNum - node.val) , abs(minNum - node.val))
        maxNum = max(node.val , maxNum)
        minNum = min(node.val , minNum)
        for ch in node.left,node.right:
            if ch:
                dfs(ch,minNum,maxNum)
    dfs(root,root.val,root.val)
    return ret
