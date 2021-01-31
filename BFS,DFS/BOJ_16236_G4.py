import sys
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,-1,1]

n= int(input())
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited= [[False for _ in range(n)] for _ in range(n)]
#time과 size,cnt 를 모두 고려해야한다
def bfs(start_x,start_y,arr,size):
	global time
	answer=deque()
	queue=deque()
	queue.append((start_x,start_y,0))
	visited[start_x][start_y]=True
	while queue:
		x,y,time = queue.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				#size가 같거나 작은 경우 지나갈 수 있음
				if not visited[nx][ny] and size>=arr[nx][ny]:
					visited[nx][ny] = True
					# 사이즈가 작을 경우 먹는다
					if 0<arr[nx][ny]<size:
						answer.append((nx,ny,time+1))
					#size가 같을 경우 
					else:
						queue.append((nx,ny,time+1))
	#최단 거리, 같은 거리일경우 x,y순서대로 오름차순 정렬
	if len(answer)>=1:
		answer=sorted(answer, key= lambda x: (x[2],x[0],x[1]))
		arr[answer[0][0]][answer[0][1]] = arr[start_x][start_y]
		arr[start_x][start_y] = 0
		time = answer[0][2]
		return True
	return False



size=2
cnt=0
ans=0
while True:
	start_x=start_y=0
	visited=[[False]*n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if arr[i][j]==9:
				start_x=i
				start_y=j
	#자신의 size만큼 먹을 경우 size up
	flag = bfs(start_x, start_y, arr, size)
	if flag:
		cnt+=1
		ans+=time
		if cnt == size:
			cnt = 0
			size += 1
	else: break
print(ans)

