# g1 백조의 호수
import sys
input = sys.stdin.readline
from collections import deque

r, c= map(int, input().split())
graph = []
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for i in range(r):
    graph.append(list(map(str, input().strip())))


def bfs():
    temp =list()
    while swan:
        x,y = swan.popleft()
        temp.append((x,y))
        #다른 백조를 만난다면 true
        if graph[x][y]=="L":
            if x!=startX or y!=startY:
                return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and graph[nx][ny] != "X":
                    visited[nx][ny] = True
                    swan.append((nx,ny))
    #다시 swan에 add시켜준다
    while temp:
        x,y = temp.pop()
        swan.append((x,y))
    return False

#녹아야 할 지점들 체크
def melted():
    hasmelted = list()
    #ice에 얼음부분만 모아둬서 시간 감축
    for i in range(len(ice)):
        x, y = ice.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == ".":
                    hasmelted.append((x, y))
                else:
                    ice.append((x, y))
    while hasmelted:
        x,y = hasmelted.pop()
        graph[x][y] ="."

day=0
ice = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j]== "L":
            startX= i
            startY= j
        if graph[i][j]=="X":
            ice.append((i,j))
swan = deque()
swan.append((startX,startY))

visited= [[False]*c for i in range(r)]
visited[startX][startY]= True

while True:
    isConnected = bfs()
    if isConnected:
        print(day)
        sys.exit()
    melted()
    day+=1