def solution(s):
    n = len(s)
    ans = 0
    for i in range(n - 1):
        for j in range(i+1,n):
            s1 = s[0:i]
            s2 = s[i:j]
            s3 = s[j:]
            if (s1 + s2) != (s2 + s3) and (s3 + s1) != (s2 + s3) and (s1+s2) != (s3 + s1):
                ans += 1
    return ans