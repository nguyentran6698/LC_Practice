from collections import defaultdict

def mostPopularCreator(creators,ids,views):
    res = []
    d = defaultdict(int)
    w = defaultdict(list)
    dMax = defaultdict(int)
    for index,name in enumerate(creators):
        # save value with current ids
        d[name] += views[index]
        dMax[name] = max(dMax[name] , views[index])
        w[name].append((ids[index],views[index]))
    print(dMax)
    # now we check for k and v
    # find the maxVal
    maxVal = 0
    for v in d.values():
        maxVal = max(v,maxVal)
    for k,v in d.items():
        lex = 0
        values = w[k]
        if len(values) > 1:
            minVal = "zzzzzzzzzz"
            for i in range(len(values)):
                print(values[i][1])
                view = values[i][1]
                val = values[i][0]
                if view == dMax[k] and minVal > val:
                    lex = i
                    print(minVal)
                    minVal = values[i][0]
                   
        if v == maxVal:
            res.append([k,w[k][lex][0]])
    print(res)
    return res 


creators = ["alice","alice","alice"]
ids = ["a","b","c"]
views = [1,2,2]
mostPopularCreator(creators,ids,views)


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        videos = collections.defaultdict(list)
        popularity = collections.defaultdict(int)
        n = len(creators)
        for i in range(n):
            videos[creators[i]].append([ids[i], views[i]])
            popularity[creators[i]] += views[i]
            
        max_views = max(popularity.values())
        res = []
        for creator, lst in videos.items():
            # print(lst)
            if popularity[creator] == max_views:
                vids = sorted(lst, key=lambda x: (-x[1], x[0]))
                # print("vids =", vids)
                res.append([creator, vids[0][0]])
                
        return res

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m = {}
        n = len(creators)
        maxviews = 0
        for i in range(n):
            c = creators[i]
            id = ids[i]
            v = views[i]
            if c not in m:
                m[c] = [v, id, v]
            else:
                m[c][0] += v
                if (m[c][2] < v) or (m[c][2] == v and m[c][1] > id):
                    m[c][1] = id
                    m[c][2] = v
            maxviews = max(maxviews, m[c][0])
 
        ans = []
        for key, value in m.items():
            if value[0] == maxviews:
                ans += [[key, value[1]]]
        return an