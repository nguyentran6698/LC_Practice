# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def tree(left,right,inorder_map_index):
            if left > right:
                return None
            nonlocal pre_order_index
            val = preorder[pre_order_index]
            pre_order_index += 1
            root = TreeNode(val)
            root.left = tree(left,inorder_map_index[val] - 1,inorder_map_index)
            root.right = tree(inorder_map_index[val] + 1 , right , inorder_map_index)
            return root 
        pre_order_index = 0
        inorder_map_index = {}
        for idx,e in enumerate(inorder):
            inorder_map_index[e] = idx
        
        return tree(0,len(preorder)-1,inorder_map_index)