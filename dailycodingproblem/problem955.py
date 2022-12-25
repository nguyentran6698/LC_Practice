class Tree:
    def __init__(self,value = 0 , left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
def solution(root):
    # We want to perform inorder traversal
    #           *
    #          / \
    #         +   +
    #       /  \ / \
    #      3   4 5  7
    d ={
        "+": lambda x , y : x + y ,
        "-": lambda x,y : x - y,
        "*": lambda x,y : x * y,
        "/": lambda x,y : x / y
    }     
    def postorder(root):
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            return root.val
        
        left = postorder(root.left)
        right = postorder(root.right)
        return d[root.val](left,right)

    return postorder(root)

root = Tree("*")
root.left = Tree("+")
root.right = Tree("+")
root.left.left = Tree(3)
root.left.right = Tree(4)
root.right.left = Tree(5)
root.right.right = Tree(7)
print(solution(root))



        