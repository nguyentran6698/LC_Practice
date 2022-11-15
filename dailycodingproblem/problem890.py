def solution1(m,n)->int:
    # bottom up
    row = [1] * n
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1 , -1):
            newRow[j] = row[j] + newRow[j+1]
        
        row = newRow
    return row[0]

def solution2(m,n)->int:
    # Top down
    row = [1] * n
    for i in range(m-1):
        newRow = [1] * n
        for j in range(1,n):
            newRow[j] = row[j] + newRow[j - 1]
        row = newRow
    return row[-1]

    #####
    #####
    #####
    #####
    