def solution(root):
    all_sum = []
    
    def get_sum(node):
        if node == None:
            return 0
        left_sum = get_sum(node.left)
        right_sum = get_sum(node.right)
        total_sum = left_sum  + right_sum
        all_sum.append(total_sum)
        return total_sum
    total = get_sum(root)
    ret = 0
    for x in all_sum:
        ret = max(ret , x *(total - x))
    return ret % (10 ** 9 +7)

    total_sum = get_sum(root)