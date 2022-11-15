
str1 = "h"
str2 = "sitting"
str3 = ""
from collections import Counter
def solution(str1:str , str2:str)->int:
    editDist  = 0
    # 1 choose which word to edit
    if len(str2) == 0:
        return len(str1)
    j = 0
    i = 0
    while i < len(str1):
        if (j < len(str2) and str2[j] != str1[i]) or j >= len(str2):
            editDist += 1
        j += 1
        i += 1
    while j < len(str2):
        editDist += 1
        j += 1
    
    return editDist

print(solution(str1,str3))


