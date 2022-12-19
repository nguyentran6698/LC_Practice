def solution(pattern, source):
    # O = vowvel
    # 1 = letter
    d = set("aeiouy")
    start = 0
    cnt = 0
    for end in range(len(source) + 1):
        subStr = source[end:end + len(source)] 
        valid = True
        for i in range(len(subStr)):
            if subStr[i] in d:
                if int(pattern[i]) != 0:
                    valid = False
                    break
            else:
                if int(pattern[i]) != 1:
                    valid = False
                    break
        if valid:
            cnt += 1
        start += 1
    return cnt
pattern = "00"
source = "aaaaaaaaaa"
print(solution(pattern,source))