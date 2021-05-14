#13460 구슬탈출2
#구슬을 동시에 움직이는 것애 대한 아이디어가 떠오르지 않아 다른 분의 아이디어를 참고하였다.
#구슬을 동시에 움직이기 위해서는 방향에 따라 앞에 있는 구슬이 달라지게 되는데, 구슬은 동일한 위치에 있을 수 없기 때문에
#경우의 수가 급격히 많아지기 때문이다.
# 구슬을 동시에 움직일 수 없기에 더 먼 이동거리를 이동한 구슬이 뒤에 있는 구슬이므로 nrx==nbx and nry==nby 이면
# 더 먼 거리를 이동한 구슬을 한 칸 뒤로 이동시켜준다.

import sys
input= sys.stdin.readline
from collections import deque

n,m= map(int, input().split())

graph=list()
for i in range(n):
    graph.append(list(map(str,input().strip())))
queue=deque()
visited=[[[[False]*m for i in range(n)] for i in range(m)] for i in range(n)]

def move(x,y,dx,dy):
    count=0
    #구슬의 다음 이동경로가 벽이거나 구멍으로 들어갔을 경우 loop문을 빠져나온다
    while graph[x+dx][y+dy]!="#" and graph[x][y]!="O":
        x+=dx
        y+=dy
        count+=1
    return x,y, count

def bfs():
    while queue:
        rx,ry,bx,by,cnt= queue.popleft()
        if cnt>10:
            break
        visited[rx][ry][bx][by]=True
        for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
            nrx, nry, red_cnt= move(rx,ry,dx,dy)
            nbx, nby, blue_cnt= move(bx,by,dx,dy)
            #파란공이 들어가면 안되기 때문에 continue
            if graph[nbx][nby]=="O":
                continue
            #파란공의 경우를 위해서 처리해주었기 때문에 빨간공만 들어간 경우이다.
            if graph[nrx][nry]=="O":
                print(cnt)
                return
            #두 구슬이 같은 위치에 있을경우, 더 먼거리를 이동한 구슬을 한칸 뒤로 이동시켜준다
            if nrx==nbx and nry==nby:
                if red_cnt>blue_cnt:
                    nrx-=dx
                    nry-=dy
                else:
                    nbx-=dx
                    nby-=dy
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby]=True
                queue.append((nrx,nry,nbx,nby,cnt+1))
    print(-1)


for i in range(n):
    for j in range(m):
        if graph[i][j]=="R":
            rx,ry= i,j
        elif graph[i][j]=="B":
            bx,by=i,j
visited[rx][ry][bx][by]=True
queue.append((rx,ry,bx,by,1))
bfs()