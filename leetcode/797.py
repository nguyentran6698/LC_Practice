from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def backtrack(path, currentNode):
            path.append(currentNode)
            if currentNode == (n - 1):
                res.append(path[:])
            else:
                for x in graph[currentNode]:
                    backtrack(path, x)
                    path.pop()

        backtrack([], 0)
        return res

    # dfs
    def allPathsSourceTarget2(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        @cache
        def all_paths(currentNode):
            if currentNode == target:
                return [[target]]
            paths = []
            for x in graph[currentNode]:
                for path in all_paths(x):
                    paths.append([currentNode] + path)
            return paths

        return all_paths(0)
