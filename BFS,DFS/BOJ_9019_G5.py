from collections import deque
import sys

n = int(input())
dslr = ["D", "S", "L", "R"]
visited=[False for _ in range(10000)]

def bfs(start, end):
	queue = deque()
	queue.append((start, ""))
	visited[start]=True
	while queue:
		x, command = queue.popleft()
		visited[x] = True
		if x == end:
			return command
		for i in dslr:
			if i == "D" and not visited[x]:
				x = x*2 if x < 10000 else x % 10000
				queue.append((x, command+"D"))
			if i == "S" and not visited[x]:
				x = x-1 if x > 0 else 9999
				queue.append((x, command+'S'))
			if i == "L" and not visited[x]:
				x = int(str(x)[1:]+str(x)[0])
				queue.append((x, command+'L'))
			if i == "R" and not visited[x]:
				x == int(str(x)[-1]+str(x)[1:3])
				queue.append((x, command+'R'))


for i in range(n):
	start, end = map(int, sys.stdin.readline().split())
	print(bfs(start, end))

