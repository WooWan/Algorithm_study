import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
answer=-1
arr=list()
for i in range(n):
	arr.append(list(map(int,sys.stdin.readline().strip())))

def bfs(x,y,w):
	visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
	depth= [[[0]*2 for _ in range(m)] for _ in range(n)]
	queue=deque()
	queue.append((x,y,w))
	visited[x][y][w]=True
	depth[x][y][w]=1
	while queue:
		x,y,w= queue.popleft()
		if x==n-1 and y==m-1: return depth[x][y][w] 
		for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
			nx=dx+x
			ny=dy+y
			if 0<=nx<n and 0<=ny<m:
				if not visited[nx][ny][w]:
					if arr[nx][ny]==1 and w==1:
						visited[nx][ny][0]=True
						depth[nx][ny][0]= depth[x][y][1]+1
						queue.append((nx,ny,0))
					elif arr[nx][ny]==0:
						visited[nx][ny][w]=True
						depth[nx][ny][w]= depth[x][y][w]+1
						queue.append((nx,ny,w))
	return -1
			
print(bfs(0,0,1))
