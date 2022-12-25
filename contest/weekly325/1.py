def solution(words,target,start):
    n = len(words)
    minDis = float("inf")
    i = start + 1
    cnt = 0 
    found = False
    if words[start] == target:
        return 0
    while i != start:
        # move foward
        cnt += 1
        if words[i] == (target):
            found = True
            minDis = min(minDis ,cnt)
            break
        i = (i + 1) % n
       
    cnt = 0
    i = start - 1
    while i != start:
        # move foward
        cnt += 1
        if words[i] == (target):
            found = True
            minDis = min(minDis , cnt)
            break
        i = (i - 1 + n) % n
    if found:
        return minDis
    return -1

words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8

print(solution(words,target,startIndex))