#전형적인 bfs 최단거리 구하기 문제
# 이런 전형적인 문제는 빨리 풀어버리자.

import sys
from collections import deque
n, m, k, x= map(int, sys.stdin.readline().split())

def bfs(visited,start, dis, cnt,ans):
	queue= deque([start])
	visited[start]=0
	while queue:
		a=queue.popleft()
		if visited[a]==dis:
			return
		for i in graph[a]:
			if visited[i]==-1:
				queue.append(i)
				visited[i]=visited[a]+1


graph=[[] for _ in range(n+1)]
visited= [-1]*(n+1)
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
ans=list()
bfs(visited,x,k,0,ans)

for idx, d in enumerate(visited):
	if d==k: ans.append(idx)
ans.sort()
if not ans: print(-1)
else:
	for i in ans:
		print(i)

