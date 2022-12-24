from ast import List
def solution(a) -> int:
    # Run from the top to bottom
    res = 0
    for i in range(len(a)):
        if a[i] != 1:
            continue
        # at i position go upward
        cnt = 0
        for j in range(i+1, len(a)):
            if a[j] == -1:
                res = max(res,cnt)
                break
            # stop when hit 1
            elif a[j] == 1:
                cnt = 0
                break
            cnt += 1
        # at i position go backward
        cnt = 0
        for j in range(i-1, -1, -1):
            if a[j] == -1:
                res = max(res,cnt)
                break
            elif a[j] == 1:
                cnt = 0
                break
            cnt += 1
    return res
forts = [-1,0,-1,0,1,1,1,-1,-1,-1]
forts = [1,0,0,-1,0,0,0,0,1]
print(solution(forts))

                


    # Bottom to top