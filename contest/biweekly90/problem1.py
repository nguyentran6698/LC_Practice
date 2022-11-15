from collections import defaultdict
def oddString(words)->str:
    l = [[ord(c) for c in word] for word in words]
    d = defaultdict(int)

    for x in l:
        diff = []
        for i in range(len(x) - 1):
            diff += [x[i+1]] - [x[i]]
            d[tuple(diff)] += 1
    
    for j,x in enumerate(l):
        dif = []
        for i in range(len(x) - 1):
            dif += [x[i+1]] - [x[i]]
            if d[tuple(dif)] == 1:
                return words[j]



