def solution(s, t):
    # first remove first s and check
    cnt = 0
    for i in range(len(s)):
        if s[i].isdigit():
            temp = s[:i] + s[i+1:]
            if temp < t:
              
                cnt += 1
    
    # count till t
    for i in range(len(t)):
        if t[i].isdigit():
            temp = t[:i] + t[i+1:]
            if temp > s:
              
                cnt += 1
    
    return cnt