def solution(words):
    s = []
    cnt = 0
    for word in words:
        s.append(set(word))
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                cnt += 1
    print(cnt)
words = ["aba","aabb","abcd","bac","aabc"]
solution(words)
    