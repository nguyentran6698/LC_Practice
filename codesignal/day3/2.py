def solution(s):
    def palindromePrefix(s,start,end):
        if start == end:
            return ''
        
        for e in range(end,start + 1 , -1):
            if s[start:e] == s[start:e][::-1]:
                return palindromePrefix(s,e,end)
        return s[start:end]
    return palindromePrefix(s,0,len(s))

print(solution("aaacodedoc"))
print(solution("codesignal"))