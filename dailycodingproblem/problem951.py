# from Queue import Queue
from collections import deque
import math

def interleave(stack):
    size = len(stack)
    queue = deque()

    # append to queue
    for _ in range(size):
        queue.append(stack.pop())
    # 5 4 3 2 1
    # Now you want to move the 3 2 1 on top
    for _ in range(size // 2):
        queue.append(queue.popleft())
    print(queue)
    
    # 3 2 1 5 4
    for _ in range(math.ceil(size / 2)):
        stack.append(queue.popleft())
    
    # [3 2 1]
    # q = (5 , 4) -> now one by one we want to rotate the queue by adding the
    # number in the stack
    for _ in range(size // 2):
        queue.append(stack.pop())
        queue.append(queue.popleft())
    
    # check if are there any element in the stack
    if stack:
        queue.append(stack.pop())
    # after we finsih arranging the queue we add it back to the stack 
    while queue:
        stack.append(queue.popleft())
    return stack



print(interleave([1, 2, 3, 4, 5]))