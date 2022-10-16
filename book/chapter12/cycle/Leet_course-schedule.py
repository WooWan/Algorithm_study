import collections
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [False] * numCourses
    finished = [False] * numCourses

    def dfs(x):
        if visited[x]:
            return False
        if finished[x]:
            return True
        visited[x] = True
        for nx in graph[x]:
                if not dfs(nx):
                    return False
        finished[x] = True
        return True

    for a, b in prerequisites:
        graph[a].append(b)

    for arr in graph:
        for x in arr:
            if not dfs(x):
                return False
    return True


print(canFinish(2, [[0, 1], [1,0]]))
