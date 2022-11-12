import sys
from collections import deque
input = sys.stdin.readline

N, H, D = map(int, input().split())
visited = [[0]*N for _ in range(N)]
graph = [list(map(str, input().strip())) for _ in range(N)]

def bfs(x,y):

    queue = deque()
    queue.append([x, y, 0, H, 0])
    visited[x][y] = H

    while queue:
        x, y, path, health, umbrella = queue.popleft()
        if health == 0:
            continue

        for dx, dy in (1,0),(0,1),(-1,0),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == "E":
                    return path+1
                if graph[nx][ny]== "U":
                    umbrella = D
                if umbrella + health -1 > visited[nx][ny]:
                    visited[nx][ny] = umbrella + health -1
                    if umbrella >= 1:
                        queue.append([nx, ny, path+1, health, umbrella-1])
                    else:
                        queue.append([nx, ny, path+1, health-1, umbrella])
    return -1

for i in range(N):
    for j in range(N):
        if graph[i][j] == "S":
            print(bfs(i,j))