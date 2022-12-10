def solution(arr):
    ret = 0
    for w in arr:
        try:
            w = int(w)
        except:
            w = len(w)
        ret = max(ret, w)
    return ret


strs = ["alic3", "bob", "3", "4", "00000"]
print(solution(strs))
