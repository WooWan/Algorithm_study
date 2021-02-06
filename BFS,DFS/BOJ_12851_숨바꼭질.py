#12851 숨바꼭질 2
import sys
from collections import deque

n, m = map(int, input().split())
visited = [False]*(100001)
arr = [0]*100001
answer = 0


def bfs(start, end):
	global answer
	queue = deque()
	queue.append((start, 0))
	visited[start] = True
	while queue:
		x, cnt = queue.popleft()
		if visited[end] and cnt > arr[end]:
			break
		#같은 좌표에 도달했다면,
		if x == end:
			#최단경로와 같다면
			if arr[x] == cnt:
				answer += 1
		for nx in (2*x, x+1, x-1):
			if 0 <= nx <= 100000:
				#이전에 방문하지 않은 노드라면
				if not visited[nx]:
					visited[nx] = True
					arr[nx] = arr[x]+1
					queue.append((nx, cnt+1))
				#방문하였지만 같은 시간에 도달하였을 경우
				elif visited[nx] and arr[nx] == cnt+1:
					queue.append((nx, cnt+1))


bfs(n, m)
print(arr[m])
print(answer)
