from collections import Counter
def solution1(words)->int:
    count = Counter(words)
    ans = 0
    central = False 
    for word, word_count in count.items():
        # Palindrome word
        if word[0] == word[1]:
            if word_count % 2 == 0:
                ans += word_count
            else:
                ans += word_count - 1
                central = True
        elif word[0] < word[1]:
            ans += 2 * min(word_count , count[word[1] + word[0]])
    if central:
        ans += 1
    return 2 * ans 


def solution2(words)->int:
    ans = 0 
    alphabet_size = 26
    central = False 
    count = [[0 for j in range(alphabet_size)] for i in range(alphabet_size)]
    for word in words:
        count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1
    for i in range(alphabet_size):
        if count[i][i] % 2 == 0:
            ans += count[i][i]
        else:
            ans += count[i][i] - 1
            central = True
        for j in range(i+1,alphabet_size):
            ans += 2 * min(count[i][j] , count[j][i])
        
    if central:
        ans += 1 
    return 2 * ans 


print(solution2(["ab","ty","yt","lc","cl","ab"]))