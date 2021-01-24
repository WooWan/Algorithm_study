#3중 반복문 돌려야한다
#visited방문 체크와 한턴에 한번이라도 바뀌었는지를 동시에 bool 체크해줘야한다 좋은문제
#sum(list[x][y] for x,y in temp)은 덤으로 필수적으로 꿀팁 ㅎ
#dfs로 풀 경우 재귀의 깊이가 매우 깊어져 recursionerror 발생
import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
graph = list()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
country = [[0 for i in range(n)] for j in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
temp = list()
for i in range(n):
	graph.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
	for j in range(n):
		country[i][j] = (i)*n+(j+1)


def open_country(x, y, nation, visited):
	queue=deque()
	queue.append((x,y))
	temp.append((x, y))
	visited[x][y] = True
	while queue:
		x,y=queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				if not visited[nx][ny] and l <= abs(graph[nx][ny]-graph[x][y]) <= r:
					visited[nx][ny]=True
					queue.append((nx,ny))
					temp.append((nx,ny))
	return temp


cnt = 0
while True:
	flag = False
	visited = [[False for i in range(n)] for j in range(n)]
	for i in range(n):
		for j in range(n):
			if not visited[i][j]:
				temp.clear()
				temp = open_country(i, j, country[i][j], visited)
				if len(temp) > 1:
					flag = True
					num = sum(graph[x][y] for x, y in temp)
					for x, y in temp:
						graph[x][y] = int(num/len(temp))
	if not flag: break
	cnt+=1
print(cnt)
