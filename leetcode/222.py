from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def countNodes(root: Optional[TreeNode]) -> int:
    return 1 + countNodes(root.left) + countNodes(root.right) if root else 0