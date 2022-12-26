from collections import defaultdict
def solution(a, m, k):
    cnt_sum = 0
    idx_rem = defaultdict(int)
    cnt_occurs = defaultdict(int)
    last_index = -1
    # Check for the first range
    for i in range(m):
        if a[i] in idx_rem:
            # Do something
            cnt_sum = 1
            last_index = max(last_index, idx_rem[a[i]])
        cnt_occurs[a[i]] += 1
        idx_rem[k - a[i]] = i
    
    # now we begin to do the sliding window
    for i in range(m,len(a)):
        # slide the window
        cnt_occurs[a[i - m]] -= 1
        # if there is no exist value that windown contains
        # remove it along with it rem
        if cnt_occurs[a[i-m]] == 0:
            del idx_rem[k - a[i -m]]
        
        # now we adding the new element
        if a[i] in idx_rem:
            cnt_sum += 1
            last_index = max(last_index,idx_rem[a[i]])
        # in case that duplicate that sum is = k is still in range
        elif last_index > i - m:
            cnt_sum += 1
        cnt_occurs[a[i]] += 1
        idx_rem[k - a[i]] = i

    return cnt_sum
a = [20, 30, 40, 20, 20, 20]
m =  5  
k = 60
print(solution(a,m,k))

# 4 7 5 3
# 1  1 0
# 0 3 2 3
# 5 5 5 5 
# 5 5 5 5   5 : 3
# 