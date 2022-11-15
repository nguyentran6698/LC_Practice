def longestPalindrome(words):
    alphabet_size = 26
    count = [[0 for _ in range(alphabet_size)] for _ in range(alphabet_size)]

    for word in words:
        count[ord(word[0]) - ord('a')][ord(word[1]) - ord('a')] += 1
    ans = 0
    central = False 
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

from collections import Counter 
def longestPalindrome2(words):
    count = Counter(words)
    ans = 0
    central = False

    for word , count_word in count.items():
        if word[0] == word[1] :
            if count_word % 2 == 0 :
                ans += count_word
            else:
                ans += count_word  - 1
                central = True

        elif word[0] < word[1]:
            ans += 2 * min(count_word , count[word[1] + word[0]])
    if central:
        ans += 1
    return 2 * ans 


words = ["ab","ty","yt","lc","cl","ab"]
words = ["cc","ll","xx"]
words = ["lc","cl","gg"]
print(longestPalindrome(words))