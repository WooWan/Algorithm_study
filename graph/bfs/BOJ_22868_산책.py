import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    x.sort()

s, e = map(int, input().split())

def bfs(x, destination):
    visited[x] = True
    queue = deque()
    queue.append((x, 0, [x]))

    while queue:
        x, count, path = queue.popleft()
        if x == destination:
            return [count, path]

        for nx in graph[x]:
            if not visited[nx]:
                visited[nx]= True
                queue.append((nx, count+1, path + [nx]))



result = 0
count, path = bfs(s, e)
result += count

visited = [False] * (n+1)
for x in path:
    if x != s and x != e:
        visited[x] = True

count, path = bfs(e, s)

print(result + count)