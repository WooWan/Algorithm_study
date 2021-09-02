import sys, heapq
from collections import deque
input = sys.stdin.readline
#아기상어 g4
n= int(input())
arr= list()
size= 2
for i in range(n):
	arr.append(list(map(int, input().split())))

def bfs(x,y, result, size, eat):
	visited = [[False]*n for i in range(n)]
	arr[x][y] = 0
	visited[x][y]=True
	queue = deque()
	heap=list()
	queue.append((0, x, y))
	while queue:
		count, x, y = queue.popleft()
		for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
			nx = x + dx
			ny = y + dy
			if 0<=nx<n and 0<=ny<n:
				if not visited[nx][ny] and arr[nx][ny]<=size:
					visited[nx][ny] = True
					# 빈 칸이거나 사이즈가 같을 경우
					if arr[nx][ny]== 0 or arr[nx][ny]==size:
						queue.append((count+1,nx,ny))
					# 사이즈가 더 작을 경우 heap 에 넣는다.
					elif 0<arr[nx][ny]<size:
						heapq.heappush(heap, (count+1,nx, ny))
	if heap:
		count, nx,ny = heapq.heappop(heap)
		result += count
		eat+=1
		if size == eat:
			size+=1
			eat=0
		bfs(nx,ny, result, size, eat)
	else:
		print(result)


for i in range(n):
	for j in range(n):
		if arr[i][j]==9:
			bfs(i,j,0,2 ,0)








#
#
#
# n= int(input())
# arr=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(arr)
# def bfs(start_x,start_y,arr,size):
# 	answer=deque()
# 	queue=deque()
# 	queue.append((start_x,start_y,0))
# 	visited[start_x][start_y]=True
# 	while queue:
# 		x,y,time = queue.popleft()
# 		for dx,dy in (1,0),(0,1), (-1,0), (0,-1):
# 			nx=x+dx
# 			ny=y+dy
# 			if 0<=nx<n and 0<=ny<n:
# 				#size가 같거나 작은 경우 지나갈 수 있음
# 				if not visited[nx][ny] and size>=arr[nx][ny]:
# 					visited[nx][ny] = True
# 					# 사이즈가 작을 경우 먹는다
# 					if 0<arr[nx][ny]<size:
# 						answer.append((nx,ny,time+1))
# 					#size가 같을 경우
# 					else:
# 						queue.append((nx,ny,time+1))
# 	#최단 거리, 같은 거리일경우 x,y순서대로 오름차순 정렬
# 	if len(answer)>=1:
# 		answer=sorted(answer, key= lambda x: (x[2],x[0],x[1]))
# 		return answer[0]
# 	return None
#
# start_x = start_y = 0
# for i in range(n):
# 	for j in range(n):
# 		if arr[i][j] == 9:
# 			start_x = i
# 			start_y = j
#
# size=2
# cnt=0
# ans=0
# while True:
# 	visited=[[False]*n for _ in range(n)]
# 	#자신의 size만큼 먹을 경우 size up
# 	arr[start_x][start_y]=0
# 	sea = bfs(start_x, start_y, arr, size)
# 	if sea is None:
# 		print(ans)
# 		sys.exit()
# 	else:
# 		start_x,start_y,time= sea
# 		cnt+=1
# 		ans+=time
# 		if cnt == size:
# 			cnt = 0
# 			size += 1
# print(ans)
# #
