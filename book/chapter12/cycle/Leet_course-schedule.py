from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [False for _ in range(numCourses)]
    finished = [False] * numCourses

    def dfs(x):
        if finished[x]:
            return True
        if visited[x] and not finished[x]:
            return False
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


print(canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))
