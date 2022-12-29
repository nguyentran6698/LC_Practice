from collections import Counter
def getMinimumMoves(word):
    res = 0
    cnt = Counter(word)
   
    for i in range(len(word)):
        x = word[i]
        if cnt[x] > 1:
            cnt[x] -= 1
            res += 1
    return res 
print(getMinimumMoves("abaaa"))