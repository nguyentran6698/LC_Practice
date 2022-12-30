from collections import defaultdict
import math
def solution(b):
    mydict = defaultdict(int)
    cnt = 0
    for i in range(len(b)):
        sn = "".join(sorted(str(b[i])))
        mydict[sn] += 1

    for k in mydict:
        n = mydict[k]
        if n>=2:
            paircombinations = math.factorial(n)//(2*(math.factorial(n-2)))
            cnt += paircombinations
    return cnt