#2636 치즈 dfs로 시도 해봐야지~
import sys
input= sys.stdin.readline

sys.setrecursionlimit(100000)

n,m=map(int, input().split())

array=list()
for i in range(n):
    array.append(list(map(int, input().split())))

def check(x,y,array):
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx=x+dx
        ny=y+dy
        if array[nx][ny]==0:
            array[x][y]=-1
            return

def dfs(x,y,visited, array):
    visited[x][y] = True
    for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
        nx= x+dx
        ny= y+dy
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                if array[nx][ny]==1:
                    visited[nx][ny] = True
                    #0으로 설정해주면 다음 dfs 탐색 때 영향을 받으므로 영향을 받지 않는 -1로 설정해주었다.
                    array[nx][ny]=-1
                elif array[nx][ny]==0:
                    dfs(nx,ny, visited,array)
preCount=0
count=0
time=0
while True:
    preCount=count
    count=0
    visited=[[False]*m for i in range(n)]
    visited[0][0]=True

    dfs(0,0,visited, array)
    for i in range(n):
        for j in range(m):
            if array[i][j]==-1:
                count+=1
                array[i][j]=0
    # 만약 치즈가 없다면 반복문을 탈출한다.
    if count==0:
        break
    time+=1
print(time)
print(preCount)
