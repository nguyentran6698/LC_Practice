def solution(queryType,query):
    h = {}
    offSetK = [0] * len(query)
    offSetV = [0] * len(query)
    cnt = 0
    for i in range(len(queryType)):
        typeQ = queryType[i]
        if typeQ == "insert":
            k,v = query[i]
            h[k] = v
        elif typeQ == "addToValue":
            offSetV += query[i][0]
        elif typeQ == "addToKey":
            offSetK += query[i][0]
        else:
            k = query[i][0] - offSetK
            cnt += (h[k] + offSetV)
    return cnt

queryType = ["insert","insert","addToValue","addToKey","get"]
queryType = ["insert","addToValue","get","insert","addToKey","addToValue","get"]
query = [[1,2],[2,3],[2],[1],[3]]
query = [[1,2],[2],[1],[2,3],[1],[-1],[3]]

print(solution(queryType,query))