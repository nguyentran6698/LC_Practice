def solution(list1, list2):
    vis = set()
    temp = list1
    while temp:
        vis.add(temp.val)
        temp = temp.next

    temp = list2
    while temp:
        if temp.val in vis:
            return temp.val
        vis.add(temp.val)

    return -1
