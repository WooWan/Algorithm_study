import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node,visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i,visited)

visited = [False] * (n + 1)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        count += 1
        dfs(i,visited)
print(count)

