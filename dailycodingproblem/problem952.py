from collections import Counter, defaultdict
def solution(string):
    def recur(counter, word_chars , word_list):
        if sum(counter.values()) == 0:
            return word_list
        else:
            for i,word in enumerate(word_chars,1):
                if all(counter.get(letter,0) >= word[letter] for letter in word):
                    new_counter = {letter:counter[letter] - word[letter] for letter in counter}

                    res = recur(new_counter, word_chars , word_list + [i])
                    if res:
                        return res
            return None
    letter_counts = Counter(string)
    words = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight", "nine"]
    words_dicts = [Counter(word) for word in words]
    res = recur(letter_counts,words_dicts,[])
    if not res:
        return None
    
    int_counts = {i:0 for i in range(10)}
    for num in res:
        int_counts[num] += 1
    return "".join(str(i) * int_counts[i] for i in range(10))

# O(n^2) since we need to check for all number

# Optimization solution
def solution2(string):
    letters_count = Counter(string) 
    int_ocurrs = {i:0 for i in range(10)}

    # first pass unique letter that match with unique number
    int_ocurrs[0] = letters_count['z']
    int_ocurrs[2] = letters_count['w']
    int_ocurrs[6] = letters_count['x']
    int_ocurrs[4] = letters_count['u']
    int_ocurrs[8] = letters_count['g']

    # second pass unique letter
    # since these letter will appear in one more number need to subtract
    int_ocurrs[3] = letters_count['h'] - int_ocurrs[8]   
    int_ocurrs[5] = letters_count['f'] - int_ocurrs[4]
    int_ocurrs[7] = letters_count['s'] - int_ocurrs[6]

    # this third pass will has more than one number
    int_ocurrs[1] = letters_count['o'] - int_ocurrs[2] - int_ocurrs[0]
    int_ocurrs[9] = letters_count['i'] - int_ocurrs[5] - int_ocurrs[6] - int_ocurrs[8]

    return ''.join(str(i)*int_ocurrs[i] for i in range(10))



print(solution2("zerozerozero"))

print(solution2("niesevehrtfeev"))