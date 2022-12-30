class Tree:
    def __init__(self,value = 0 , left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
def solution(root):

    def dfs(root):
        if root is None:
            return 0, True

        left_count , is_left_valid = dfs(root.left)
        right_count , is_right_valid = dfs(root.right)
        total_count = left_count + right_count

        if is_left_valid and is_right_valid:
            if root.left is not None and root.left.val != root.val:
                return total_count, False
            if root.right is not None and root.right.val != root.val:
                return total_count , False
            return total_count + 1 , True
        return total_count , False
    
    count , _ = dfs(root)
    return count

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
root = Tree(0)
root.left = Tree(1)
root.right = Tree(0)
root.right.left = Tree(1)
root.right.right = Tree(0)
root.right.left.left = Tree(1)
root.right.left.right = Tree(1)

print(solution(root))