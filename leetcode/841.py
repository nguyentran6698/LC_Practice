from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(seen,key):
            if not seen[key]:
                seen[key] = True
                for k in rooms[key]:
                    dfs(seen,k)
        seen = [False] * len(rooms)
        dfs(seen,0)
        return all(seen)
