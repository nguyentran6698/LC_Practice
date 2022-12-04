def solution(sentence):
    s = sentence.split(" ")
    print(s)
    last = s[0][-1]
    if len(s) == 1:
        return last == s[0][0]
    for i in range(1,len(s)):
        if s[i][0] != last:
            return False
        last = s[i][-1]
    return True
        
s = "leetcode exercises sound delightful"
s1 = "eetcode"
print(solution(s))