# Solution 1 : Time: O(N)  Space O(N)


def reverse1(head, prev):
    if not head:
        return prev
    temp = head.next
    head.next = prev
    return reverse1(temp, head)


# Solution 2: Time O(N) Space O(1)


def reverse2(head):
    prev, current = None, head
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
