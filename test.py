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
printTable(4)

