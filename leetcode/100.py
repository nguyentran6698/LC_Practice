def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (q or p) == None:
        return True
    if p != None and q == None:
        return False
    elif p == None and q != None:
        return False
    if p.val != q.val:
        return False
    left = self.isSameTree(p.left , q.left)
    right = self.isSameTree(p.right,q.right)
    return left and right