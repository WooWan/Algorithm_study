#17472 mst 다리만들기
#그래프 탐색과 최소신장트리를 잘 섞은 문제
import sys
input=sys.stdin.readline
from collections import deque

n,m= map(int, input().split())
group= [[0]*m for i in range(n)]
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

cnt=1
def bfs(x,y,visited,cnt,group):
    queue=deque()
    queue.append((x,y))
    group[x][y]=cnt
    while queue:
        x,y=queue.popleft()
        visited[x][y]=True
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    group[nx][ny]=cnt

visited=[[False]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and not visited[i][j]:
            bfs(i,j,visited,cnt,group)
            cnt+=1

parent=[i for i in range(cnt)]
edge=[]
def dist(x,y):
    source=group[x][y]
    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
        nx,ny= x,y
        cnt=0
        while True:
            nx+=dx
            ny+=dy
            if 0>nx or nx>=n or 0>ny or ny>=m:break
            if group[nx][ny]!=0:
                if cnt>=2:
                    dest= group[nx][ny]
                    edge.append((source,dest ,cnt))
                break
            cnt+=1

for i in range(n):
    for j in range(m):
        if group[i][j]!=0:
            dist(i,j)

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[max(a,b)]=min(a,b)
edge.sort(key=lambda x:x[2])
answer=0

temp=0
for x,y,value in edge:
    if find(x)!=find(y):
        temp+=1
        union(x,y)
        answer+=value
#총 간선의 개수는 v-1개이다. 따라서 cnt-2==temp이면 모든 간선이 연결되었다고 볼 수 있다
print(answer if temp==cnt-2 else -1)