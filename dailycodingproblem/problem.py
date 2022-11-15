def solution(n:int):
    while n > 99:
        r = n / 10
        l = n - (10 * r)
        n = 5 * l + r
        return (n - 7 * (n / 7)) == 0
print(solution(448))


# Hackerrank TuSimple

def printTable(n):
    pRow = [i + 1 for i in range(n)]
    i = 0
    while i < n:
        j = 0
    
        while j < n:
            space = len(str(pRow[j] * n)) - len(str(pRow[j] * (i + 1)))
            newStr = str(pRow[j] * (i + 1)) + " " + (" " * space)
            print(newStr,end="")
            j += 1  
        print()
        i += 1
printTable(15)

