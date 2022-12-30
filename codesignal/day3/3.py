def mergeStrings(s1, s2):
    
    # record appear times
    record1 = {}
    record2 = {}
    for ch in s1:
        record1[ch] = record1.get(ch,0)+1
    for ch in s2:
        record2[ch] = record2.get(ch,0)+1
    
    # merge with two pointers
    pt1 = 0
    pt2 = 0
    len1 = len(s1)
    len2 = len(s2)
    res = []
    while pt1 < len1 and pt2 < len2:
        if record1[s1[pt1]] < record2[s2[pt2]]:
            res.append(s1[pt1])
            pt1 += 1
        elif record1[s1[pt1]] > record2[s2[pt2]]:
            res.append(s2[pt2])
            pt2 += 1
        else:
            # if equal times
            if s1[pt1] <= s2[pt2]:
                res.append(s1[pt1])
                pt1 += 1
            elif s1[pt1] > s2[pt2]:
                res.append(s2[pt2])
                pt2 += 1
                
    # continue with the remaining characters
    while pt1 < len1:
        res.append(s1[pt1])
        pt1 += 1
    
    while pt2 < len2:
        res.append(s2[pt2])
        pt2 += 1
    return "".join(res)