class newNode:
 
    # Constructor to create a newNode
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None
        self.visited = False

def solution2(root):
    def height(nodeH):
        if nodeH == None:
            return 0       
        return 1 + max(height(nodeH.left) , height(nodeH.right))
    ret = 0
    def deepNode(node,level):
        if node == None:
            return
        nonlocal ret 
        if level == 1:
            ret = node.data
        elif level > 1:
            deepNode(node.left, level - 1)
            deepNode(node.right , level - 1)
    
    deepNode(root,height(root))
    return ret





def solution1(root):
    ret = 0
    maxLevel = -1
    
    def dfs(node,level):
        if node == None:
            return
        nonlocal ret
        nonlocal maxLevel
        dfs(node.left,level + 1)
        if level > maxLevel:
            maxLevel = level
            ret = node.data
        dfs(node.right,level + 1)
    dfs(root,0)
    return ret


if __name__ == '__main__':
    root = newNode("a")
    root.left = newNode("b")
    root.right = newNode("c")
    root.left.left = newNode("d")
    print(solution1(root))
    print(solution2(root))