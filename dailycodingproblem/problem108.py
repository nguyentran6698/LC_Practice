class TreeNode:
    def __init__(self, val):
        self.root = None
        self.left = None
        self.right = None
        self.val = val


def solution(nums):
    def helper(left, right):
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums))
