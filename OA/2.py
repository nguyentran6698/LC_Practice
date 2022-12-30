import heapq
def getMaximumAmount(quantity, m):
    # Write your code here
    quantity = [-x for x in quantity]
    heapq.heapify(quantity)
    res = 0
    for _ in range(m):
        x = (-1) * heapq.heappop(quantity)
        res += x
        heapq.heappush(quantity,(-1) * (x - 1))
    
    return res
quantity=[1,2,4]
m = 4
print(getMaximumAmount(quantity,m)) 